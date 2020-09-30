from django.shortcuts import get_object_or_404, render

from .models import Listing


def index(request):
    listings = Listing.objects.all()

    context = {'listings': listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    lis = get_object_or_404(Listing, pk=listing_id)

    context = {'listing': lis}

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
