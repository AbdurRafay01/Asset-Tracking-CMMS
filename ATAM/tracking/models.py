from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    phone_number=models.IntegerField('User phone number ',default=0,null=False,help_text="Number format:0300-1234567")

    def __str__(self):
        return  self.username

class Tracker(models.Model):
    name = models.CharField('Tracker name ',max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.name
class Location(models.Model):
    tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE,verbose_name='related tracker')
    lat = models.DecimalField('Tracker latitude value',max_digits=8,decimal_places=4)
    lng = models.DecimalField('Tracker longitude value',max_digits=8,decimal_places=4)

    def __str__(self):
        return  self.tracker.name