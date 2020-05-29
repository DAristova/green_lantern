from django.db import models


class CarQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')


class CarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('model', 'model__brand')
