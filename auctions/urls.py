from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newListing", views.newListing, name="newListing"),
    path("listing_page/<str:listing_id>", views.listing_page, name="listing_page"),
    path("new_bid/<str:listing_id>", views.new_bid, name="new_bid"),
    path("change_watchlist/<str:listing_id>/<str:reverse_method>", views.change_watchlist, name="change_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close_bid/<str:listing_id>", views.close_bid, name="close_bid"),
    path("comment/<str:listing_id>", views.comment, name="comment"),
    path("category_view/<str:category>", views.category_view, name="category_view")
]