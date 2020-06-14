# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    counrty = models.ForeignKey('Country', on_delete=models.SET_NULL, db_column='counrty', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, db_column='menu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Personal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL(), db_column='restaurant', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)
    counrtry = models.ForeignKey(Country, on_delete=models.SET_NULL, db_column='counrtry', blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, db_column='menu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'
