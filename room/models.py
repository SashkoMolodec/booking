from django.db import models

from hotel.models import Hotel


class Room(models.Model):
    number = models.IntegerField()
    roommates_allowed = models.IntegerField()
    rooms = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # ManyToOne
