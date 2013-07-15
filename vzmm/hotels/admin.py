from django.contrib import admin
from hotels.models import Hotel, Address, Review

from django.forms.models import BaseInlineFormSet

class AddressInline(admin.StackedInline):
    model = Address

class ReviewInline(admin.StackedInline):
    model = Review

class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields':['name', 'tag', 'description', 'url',
            'starting_rate', 'comment', 'created_date']
            }),
    ]
    inlines = [AddressInline, ReviewInline]

admin.site.register(Hotel, HotelAdmin)
