from django.db import models

from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField


SCORE_CHOICES = (
    (1.0, _(u"*")),
    (2.0, _(u"**")),
    (3.0, _(u"***")),
    (4.0, _(u"****")),
    (5.0, _(u"*****")),
)

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=15, blank=True)
    url = models.URLField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    comment = models.CharField(max_length=100, blank=True)
    starting_rate = models.DecimalField(max_digits=6, decimal_places=2,
        blank=True, null=True)
    created_date = models.DateTimeField('date created')

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
    position = GeopositionField()

    def __unicode__(self):
        return ' '.join([
            self.address,
            self.city,
            ])


class Review(models.Model):
    """A ``Review`` consists on a comment and a rating.
    """
    hotel = models.ForeignKey(Hotel, null=True, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    user_email = models.EmailField(blank=True)
    user_city = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)
    score = models.FloatField(choices=SCORE_CHOICES, default=3.0)
    active = models.BooleanField(default=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-creation_date", )

    def __unicode__(self):
        return "%s (%s)" % (self.user_name, self.score)

