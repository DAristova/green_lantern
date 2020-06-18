from django.db import models


class OrderQuerySet(models.QuerySet):
    def reserved(self):
        return self.filter(status="Reserved")

    def in_processing(self):
        return self.filter(status="Process")

    def success(self):
        return self.filter(status="Success")

    def canceled(self):
        return self.filter(status="Canceled")

    def archived(self):
        return self.filter(status="Archived")
