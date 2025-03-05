from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username + " " + self.first_name + " " + self.last_name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=255, null=True, blank=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def get_drivers(self) -> list[Driver]:
        return list(self.drivers.all())
