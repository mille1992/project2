from django.contrib import admin, auth

from .models import Listing, Comment, Bid



# Register your models here.
## This enables manipulation in admin screen of those models
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)
