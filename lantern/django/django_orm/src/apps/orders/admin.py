from django.contrib import admin
from src.apps.orders.models import Order


@admin.register(Order)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'status', )
