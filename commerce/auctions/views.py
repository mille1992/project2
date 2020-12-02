from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment


def index(request):
    allListings = list(Listing.objects.all())
    if not allListings:
        raise Http404("No Listings found")
    else: 
        return render(request, "auctions/index.html", {
            "listings": allListings
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

def createListing(request):
    if request.method == "POST":
        # get data from POST request
        titleInput = request.POST["titleInput"]
        descriptionInput = request.POST["descriptionInput"]
        startPrizeInput = request.POST["startPrizeInput"]
        imageUrlInput = request.POST["imageUrlInput"]
        categoriesInput = request.POST["categoriesInput"]
        #create new object from data
        newListing = Listing(title=titleInput, description=descriptionInput, listingPrize=startPrizeInput, imageUrl=imageUrlInput, category=categoriesInput) 
        #save data to db
        newListing.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createListing.html")

def listingDetails(request, listingId):
    listing = list(Listing.objects.filter(id = listingId))
    if "watchlist" not in request.session:
        request.session["watchlist"] = []
        watchlist = request.session["watchlist"]
    else:
        watchlist = request.session["watchlist"]
    
    if listing[0].id not in watchlist:
        itemInWatchlist = False
    else:
        itemInWatchlist = True


    if request.method == "POST":
        if listing[0].id not in watchlist and itemInWatchlist == False:
            watchlist.append(listing[0].id)
            request.session["watchlist"] = watchlist
            itemInWatchlist = True
        else:
            watchlist.remove(listing[0].id)
            request.session["watchlist"] = watchlist
            itemInWatchlist = False

        return render(request, "auctions/listingDetails.html", {
            "listing": listing[0],
            "watchlistCheck": itemInWatchlist
        })
    else:        
        return render(request, "auctions/listingDetails.html", {
            "listing": listing[0],
            "watchlistCheck": itemInWatchlist
        })