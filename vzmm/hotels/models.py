from django.db import models
from ratings.models import Ratings

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=15, blank=True)
    url = models.URLField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    comment = models.CharField(max_length=100, blank=True)
    starting_rate = models.DecimalField(max_digits=6, decimal_places=2,
        blank=True, null=True)
    created_date = models.DateTimeField('date created')
    ratings = Ratings()

    def __unicode__(self):
        return self.name



class Address(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    email2 = models.EmailField(max_length=75, blank=True)

    def __unicode__(self):
        return ' '.join([
            self.address,
            self.city,
            ])
