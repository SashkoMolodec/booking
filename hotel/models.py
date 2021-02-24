from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(default='very cool hotel!')
    country = models.TextField()
    capacity = models.DecimalField(decimal_places=0, max_digits=1000)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    hotels = models.ManyToManyField(Hotel)
