from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db.models import Index

from src.apps.orders.managers import OrderQuerySet


class Order(models.Model):
    STATUS_RESERVED = 'reserved'
    STATUS_PROCESS = 'process'
    STATUS_SUCCESS = 'success'
    STATUS_CANSELED = 'canceled'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_RESERVED, "Reserved"),
        (STATUS_PROCESS, "Process"),
        (STATUS_SUCCESS, "Success"),
        (STATUS_CANSELED, "Canceled"),
        (STATUS_ARCHIVED, "Archived"),
    )

    order_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(to='cars.Car', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_RESERVED, blank=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=200)

    objects = OrderQuerySet.as_manager()

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

        indexes = [
            Index(fields=['status', ])
        ]
