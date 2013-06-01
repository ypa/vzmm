
from hotels.models import Hotel
from django.shortcuts import render


def index(request):
    latest_hotel_list = Hotel.objects.order_by('-created_date')[1:5]
    classified_hotel_list = Hotel.objects.filter(tag='classified')\
                            .order_by('-created_date')[:4]
    featured_hotel = Hotel.objects.order_by('-created_date')[0]
    context = {
                'latest_hotel_list': latest_hotel_list,
                'classified_hotel_list': classified_hotel_list,
                'featured_hotel': featured_hotel
                }
    return render(request, 'home.html', context)