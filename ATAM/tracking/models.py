from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid
# Create your models here.

class User(AbstractUser):
    phone_number=models.IntegerField(default=0,null=False,help_text="Number format:0300-1234567")


class Tracker(models.Model):
    pass #
class Location(models.Model):
    #track_id = ye forign key hogi tracker class ki ki
    lat = models.DecimalField(max_digits=8,decimal_places=4)
    lng = models.DecimalField(max_digits=8,decimal_places=4)