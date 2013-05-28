

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from hotels.models import Hotel

def index(request):
    latest_hotel_list = Hotel.objects.order_by('-created_date')[:5]
    context = {'latest_hotel_list': latest_hotel_list}
    return render(request, 'hotels/index.html', context)

def detail(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404
    return render(request, 'hotels/detail.html', {'hotel': hotel})

