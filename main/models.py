from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=254, primary_key=True)
    login_date = models.DateTimeField(
            blank=True, null=True)

    # def add(self):
    #     self.login_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name
