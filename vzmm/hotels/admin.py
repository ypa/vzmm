from django.contrib import admin
from hotels.models import Hotel, Address

from django.forms.models import BaseInlineFormSet

class AddressInline(admin.StackedInline):
    model = Address

class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields':['name', 'tag', 'description', 'starting_rate',
            'comment', 'created_date']
            }),
    ]
    inlines = [AddressInline]

admin.site.register(Hotel, HotelAdmin)
