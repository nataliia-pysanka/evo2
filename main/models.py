from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=254, primary_key=True)
    # email = models.TextField(primary_key=True, unique=True)
    # email = models.EmailField(primary_key=True, unique=True)
    # login_date = models.DateTimeField(
    #         blank=True, null=True)

    # def __init__(self):
    #     self.login_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name
