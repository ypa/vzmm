

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
    def round_to(n, precission):
        correction = 0.5 if n >= 0 else -0.5
        return int(n/precission+correction)*precission

    def round_to_point_5(n):
        return round_to(n, 0.5)

    def calculate_average_score(reviews=None):
        n_reviews = len(reviews)
        total = sum([review.score for review in reviews])
        if n_reviews == 0:
            return 0.0
        return round_to_point_5(total/n_reviews)


    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404
    reviews = hotel.review_set.all()
    avg_score = calculate_average_score(reviews)
    n_reviews = len(reviews)
    return render(request, 'hotels/detail.html',
        {
        'hotel': hotel,
        'avg_score':avg_score,
        'n_reviews':n_reviews,
        })


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
