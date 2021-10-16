from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length = 50)
    created_date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(null = True, max_length = 250)
    flActive = models.BooleanField(default = True)
    begining_bid = models.FloatField()
    current_bid = models.FloatField(blank = True, null = True)
    category = models.CharField(max_length = 30)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "all_creators_listings")
    watchers = models.ManyToManyField(User, blank = True, related_name = "watched_listings")
    buyer = models.ForeignKey(User, null = True, on_delete = models.PROTECT)
    image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def _str_(self):
        return f"{self.title} - {self.starting_bid}"

class Bid(models.Model):
    auction = models.ForeignKey(Listing, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.CharField(max_length = 300)
    created_date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = "get_comments")

    def get_creation_date(self):
        return self.createdDate.strftime("%B %d %Y")