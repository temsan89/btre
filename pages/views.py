from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
from realtors.models import Realtor


def index(req):
    # limit 3 listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
      'listings': listings,
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      }

    return render(req, 'pages/index.html', context)

def about(req):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
      'realtors': realtors,
      'mvp_realtors': mvp_realtors
    }

    return render(req, 'pages/about.html', context)
