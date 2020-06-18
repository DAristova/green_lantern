from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=5)

    class Meta:
        db_table = 'country'
        ordering = ["name"]
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    country = models.ForeignKey(to='Country', on_delete=models.DO_NOTHING, related_name='cities', blank=True)

    class Meta:
        db_table = 'city'
        ordering = ["name"]
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    email = models.EmailField
    city = models.ForeignKey(to='City', on_delete=models.DO_NOTHING, related_name='dealers', blank=True)

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')

    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    email = models.EmailField(max_length=50, unique=True)
