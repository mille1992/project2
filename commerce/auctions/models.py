from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    startingPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
    listingPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
    imageUrl = models.CharField(max_length=128)
    category = models.CharField(max_length=64, default="others")

    def __str__(self):
        return f"Titel: {self.title}, Preis: {self.listingPrize}, Beschreibung: {self.description}"


class Bid(models.Model):
    bidPrize = models.PositiveIntegerField(validators=[MinValueValidator(0.01)])
        
    def __str__(self):    
        return f"Gebot: {self.bidPrize}"

class Comment(models.Model):
    commentContent = models.TextField()

    def __str__(self):
        return f"Comment: {self.commentContent}"