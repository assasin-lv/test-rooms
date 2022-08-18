from django.db import models
from businessEvent.constanst import *
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=M_CAPACITY)
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    type_event = models.CharField(max_length=1, choices=TYPE_EVENT_CHOICES,)
    available =  models.BooleanField(default=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,)

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

