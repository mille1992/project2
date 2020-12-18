from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    
    def __str__(self):
        return f"User: {self.username}, id: {self.id}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    startingPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
    listingPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
    imageUrl = models.CharField(max_length=128)
    category = models.CharField(max_length=64, default="others")
    listingOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listingCreator")
    listingStatus = models.CharField(max_length=64, default="open")

    def __str__(self):
        return f"Titel: {self.title}, Preis: {self.listingPrize}, Beschreibung: {self.description} by {self.listingOwner}"


class Bid(models.Model):
    bidPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
    biddingUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="biddedListing", default="9")

    def __str__(self):    
        return f"Gebot: {self.bidPrize} by {self.biddingUser}"

class Comment(models.Model):
    commentContent = models.TextField()
    commentCreator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentingUsers")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listingsCommenters", default="9")

    def __str__(self):
        return f"Comment by {self.commentCreator}: {self.commentContent}"