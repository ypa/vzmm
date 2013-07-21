

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from hotels.models import Hotel

def index(request):
    latest_hotel_list = Hotel.objects.order_by('-created_date')
    context = {'latest_hotel_list': latest_hotel_list}
    return render(request, 'hotels/index.html', context)


def detail(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404
    return render(request, 'hotels/detail.html', {'hotel': hotel})


def classifieds(request):
    classified_hotel_list = Hotel.objects.filter(tag='classified')\
                            .order_by('-created_date')
    context = {'classified_hotel_list': classified_hotel_list}
    return render(request, 'hotels/classifieds.html', context)


def rate(request, hotel_id):
    if request.method == 'POST':
        post_data = request.POST
        rating = post_data.get('value')
        msg = "Hotel number %s, rating is %s.\n" % (hotel_id, rating)
        return HttpResponse(msg)
        # use post data to complete the rating..
