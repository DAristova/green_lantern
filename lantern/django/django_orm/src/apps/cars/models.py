from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _

from .managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=15)
    name = models.CharField(max_length=15)


class CarProperty(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(to='Property', on_delete=models.DO_NOTHING, null=True, blank=False)
    car = models.ForeignKey(to='Car', on_delete=models.DO_NOTHING, null=True, blank=False)


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    car_id = models.AutoField(primary_key=True)
    color = models.ForeignKey(to='Color', on_delete=models.SET_NULL(), related_name='colours')
    dealer = models.ForeignKey(to='dealers.Dealer', on_delete=models.CASCADE, related_name='cars')
    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, blank=False, related_name=models)
    engine_type = models.CharField(max_length=30)
    population_type = models.CharField(max_length=30)
    price = models.FloatField(max_length=16)
    fuel_type = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    doors = models.IntegerField(blank=True)
    capasity = models.IntegerField(blank=True)
    gear_case = models.CharField(max_length=15, blank=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    number = models.CharField(max_length=16, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))
    objects = CarManager.from_queryset(CarQuerySet)()

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['status', ])
        ]
