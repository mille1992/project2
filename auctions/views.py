from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


from .models import User, Listing, Bid, Comment


def index(request):
    allListings = list(Listing.objects.all())

    if not allListings:
        #raise Http404("No Listings found")
        return render(request, "auctions/createListing.html")
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

@login_required
def createListing(request):
    if request.method == "POST":
        # get data from POST request
        titleInput = request.POST["titleInput"]
        descriptionInput = request.POST["descriptionInput"]
        startPrizeInput = request.POST["startPrizeInput"]
        imageUrlInput = request.POST["imageUrlInput"]
        categoriesInput = request.POST["categoriesInput"]
        user = User.objects.get(id=request.user.id)
        
        if titleInput != "":
            #create new object from data
            newListing = Listing(title=titleInput, description=descriptionInput, listingPrize=startPrizeInput , startingPrize=startPrizeInput, imageUrl=imageUrlInput, category=categoriesInput, listingOwner=user) 
            #save data to db
            newListing.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createListing.html")

def listingDetails(request, listingId):
    listing = Listing.objects.get(id = listingId)
    
    user = "Noone"
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    
    comments = []
    if listing.listingsCommenters.all():
        comments = listing.listingsCommenters.all()
    
    # creation of default values for checking for the max bidder
    maxBiddingUser = "Noone"
    checkMaxBidder = False
    
    # if the listing is closed and gets accessed by the highest bidder
    if listing.biddedListing.all():
        maxBiddingUser = Bid.objects.get(bidPrize=listing.listingPrize)
        if user == maxBiddingUser.biddingUser and listing.listingStatus == "closed":
            checkMaxBidder = True

    # watchlist functionality check
    if "watchlist" not in request.session:
        request.session["watchlist"] = []
        watchlist = request.session["watchlist"]
    else:
        watchlist = request.session["watchlist"]

    if listing.id not in watchlist:
        itemInWatchlist = False
    else:
        itemInWatchlist = True


    if request.method == "POST":
        # if POST request was issued by a new bid
        if "bidPrize" in request.POST:
            bidPrize = int(request.POST["bidPrize"])
            currentPrize = listing.listingPrize
            startingPrize = listing.startingPrize
            # check that prize of the bid is higher than the current and the starting Prize, if yes, save the new bid.
            if bidPrize > currentPrize and bidPrize > startingPrize:
                listing.listingPrize = bidPrize
                listing.save()
                bid = Bid(bidPrize = bidPrize, biddingUser = user, listing = listing)
                bid.save()

        # if POST request was issued by a change on the watchlist
        elif "closeAuctionButton" in request.POST: 
            listing.listingStatus = "closed"
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        # if POST request was issued by a closure of the auction
        elif "commentInput" in request.POST and request.POST["commentInput"] != "":
            comment = Comment(commentContent = request.POST["commentInput"], commentCreator = user, listing = listing)
            comment.save()
            comments = listing.listingsCommenters.all()
        else:
            #if the item is not on the watchlist, add it and change the indicator for the watchlist button
            if listing.id not in watchlist and itemInWatchlist == False: 
                watchlist.append(listing.id)
                request.session["watchlist"] = watchlist
                itemInWatchlist = True
            #if the item is on the watchlist, remove it and change the indicator for the watchlist button
            else:
                watchlist.remove(listing.id)
                request.session["watchlist"] = watchlist
                itemInWatchlist = False


        return render(request, "auctions/listingDetails.html", {
            "listing": listing,
            "watchlistCheck": itemInWatchlist,
            "currentUser": user,
            "checkMaxBidder": checkMaxBidder,
            "comments": comments
        })
    else: 
        return render(request, "auctions/listingDetails.html", {
            "listing": listing,
            "watchlistCheck": itemInWatchlist,
            "currentUser": user,
            "checkMaxBidder": checkMaxBidder,
            "comments": comments
        })

@login_required
def watchlist(request):
    watchlistIds = []
    watchlistListings = []
    if request.session["watchlist"]:
        watchlistIds = request.session["watchlist"]
        watchlistListings = list(Listing.objects.filter(id__in =  watchlistIds))


    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlistListings
    })


def categories(request):
    listings = Listing.objects.all()
    categoriesList = []
    for listing in listings:
        if listing.category not in categoriesList:
            categoriesList.append(listing.category)

    return render(request, "auctions/categories.html", {
        "categoriesList": categoriesList
    })


def categoryListings(request, category):
    listings = Listing.objects.filter(category = category)

    return render(request, "auctions/categoryListings.html", {
        "listings": listings,
        "category": category
    })

