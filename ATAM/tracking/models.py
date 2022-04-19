from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.http import JsonResponse
# Create your models here.

class User(AbstractUser):
    phone_number=models.IntegerField('User phone number ',default=0,null=False,help_text="Number format:0300-1234567")

    def __str__(self):
        return  self.username
class Asset(models.Model):
    asset_name = models.CharField('Tracker name ',max_length=30) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asset_name

class Tracker(models.Model):
    status_choices = (
        (0,"OFF"),
        (1,"ON"),
    )
    tracker = models.ForeignKey(Asset,on_delete=models.CASCADE,verbose_name='related Asset')
    status = models.IntegerField(default=0,choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.tracker.asset_name
class Location(models.Model):
    tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE,verbose_name='related tracker')
    lat = models.DecimalField('Tracker latitude value',max_digits=8,decimal_places=4)
    lng = models.DecimalField('Tracker longitude value',max_digits=8,decimal_places=4)

    def __str__(self):
        return  self.tracker.tracker.asset_name
   