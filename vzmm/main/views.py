from hotels.models import Hotel
from django.shortcuts import render

FEATURED_ID = 9

def index(request):
    latest_hotel_list = Hotel.objects.order_by('-created_date')[2:6]
    classified_hotel_list = Hotel.objects.filter(tag='classified')\
                            .order_by('-created_date')[:4]
    featured_hotel = Hotel.objects.get(id=FEATURED_ID)
    context = {
                'latest_hotel_list': latest_hotel_list,
                'classified_hotel_list': classified_hotel_list,
                'featured_hotel': featured_hotel
                }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')


def tos(request):
    return render(request, 'tos.html')
