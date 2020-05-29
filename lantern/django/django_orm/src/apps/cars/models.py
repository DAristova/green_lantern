from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]
        constraints = [
            UniqueConstraint(fields=('name',), name='unique-color')
        ]
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        constraints = [
            UniqueConstraint(fields=('name',), name='unique-car-brand')
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
        constraints = [
            UniqueConstraint(fields=('name', 'brand'), name='unique-car-model')
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Car(models.Model):
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

    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    # dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE, related_name='cars')

    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, blank=False)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))

    # other fields ...
    #

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
