from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from .models import *
from django.contrib.auth.decorators import login_required
from .models import User
import datetime
from django import forms


class newListingForm(ModelForm):

    class Meta:
        model = Listing
        fields = ["title", "description", "begining_bid", "category", "image"]


class new_bid_form(ModelForm):
    class Meta:
        model = Bid
        fields = ["offer"]


class new_comment_form(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment" : forms.TextInput(attrs={
                "class" : "form-control offset-3",
                "placeholder" : "Leave your comment here"
        })}


def index(request):
    listings = Listing.objects.filter(flActive = True)
    categories = list(set([listing.category for listing in Listing.objects.all() if listing.category]))
    return render(request, "auctions/index.html", {
        'listings' : listings,
        "categories" : categories
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def newListing(request):
    if request.method == "POST":
        form = newListingForm(request.POST, request.FILES)

        if form.is_valid():
            newListing = form.save(commit=False)
            newListing.creator = request.user
            newListing.save()

            return render(request, "auctions/newListing.html", {
                "form" : newListingForm(),
                "success" : True
            })

        else:
            return render(request, "auctions/newListing.html", {
                "form" : newListingForm()
            })

    else:
        return render(request, "auctions/newListing.html", {
                "form" : newListingForm()
            })


def listing_page(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    listing_users = listing.watchers.all()

    if listing:
        return render(request, "auctions/listing_page.html", {
            "listing" : listing,
            "new_bid_form" : new_bid_form(),
            "listing_users" : listing_users,
            "new_comment_form" : new_comment_form(),
            "comments" : listing.get_comments.all()
        })

@login_required
def new_bid(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    offer =  float(request.POST["offer"])
    if is_valid(offer, listing):
        listing.current_bid = offer
        form = new_bid_form(request.POST)
        newbid = form.save(commit=False)
        newbid.auction = listing
        newbid.user = request.user
        newbid.save()
        listing.save()
        return HttpResponseRedirect(reverse("listing_page", args = [listing_id]))
    else:
        return render(request, "auctions/listing_page.html", {
            "listing" : listing,
            "new_bid_form" : new_bid_form,
            "error" : True
        })



def is_valid(offer, listing):
    if offer>listing.begining_bid and (listing.current_bid is None or offer > listing.current_bid):
        return True
    else:
        return False


def change_watchlist(request, listing_id, reverse_method):
    listing_object = Listing.objects.get(id=listing_id)
    if request.user in listing_object.watchers.all():
        listing_object.watchers.remove(request.user)
    else:
        listing_object.watchers.add(request.user)
    if reverse_method == "listing_page":
        return listing_page(request, listing_id)
    else:
        return HttpResponseRedirect(reverse(reverse_method))


def watchlist(request):
    listings = request.user.watched_listings.all()

    for listing in listings:
        if request.user in listing.watchers.all():
            listing.is_watched = True
        else:
            listing.is_watched = False

    return render(request, "auctions/watchlist.html", {
        "listings" : listings
    })


def close_bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user == listing.creator:
        listing.flActive = False
        listing.buyer = Bid.objects.filter(auction=listing).last().user
        listing.save()
        return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))

@login_required
def comment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    form = new_comment_form(request.POST)
    new_comment = form.save(commit = False)
    new_comment.user = request.user
    new_comment.listing = listing
    new_comment.save()
    return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))


def category_view(request, category):
    listings = Listing.objects.filter(category=category, flActive=True)
    categories = list(set([listing.category for listing in Listing.objects.all() if listing.category]))
    return render(request, "auctions/index.html", {
        "listings" : listings,
        "categories_available" : True,
        "categories" : categories
    })