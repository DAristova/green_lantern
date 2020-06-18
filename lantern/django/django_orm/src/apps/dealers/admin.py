from django.contrib import admin

from .models import Country, City, Dealer


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'name', 'code')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'name', 'country')


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'city')
