

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from hotels.models import Hotel, Review
from django.http import HttpResponseRedirect
from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    score = forms.FloatField()
    comment = forms.CharField(widget=forms.Textarea)


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
        hotel = Hotel.objects.get(pk=hotel_id)
        url = '/hotels/%s/' % (hotel_id)
        form = ReviewForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            form_fields = {}
            form_fields['user_name'] = form.data['user_name']
            form_fields['user_city'] = form.data['user_city']
            form_fields['user_email'] = form.data['user_email']
            form_fields['score'] = form.data['score']
            form_fields['comment'] = form.data['comment']
            review = Review(**form_fields)
            hotel.review_set.add(review)
            hotel.save()
            return HttpResponseRedirect(url)
