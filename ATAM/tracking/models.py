from operator import mod
from django.db import models

from django.http import JsonResponse
from user.models import User
# Create your models here.




class Asset(models.Model):
    asset_name = models.CharField('Asset name ',max_length=30) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_tracker = models.OneToOneField('Tracker',on_delete=models.CASCADE,verbose_name='Assigned Tracker',blank=True,
        null=True)
    def __str__(self):
        return self.asset_name


class Tracker(models.Model):
    tracker_name = models.CharField('Tracker name ',max_length=30) 
    status_choices = (
        (0,"OFF"),
        (1,"ON"),
    )
    tracker = models.ForeignKey(Asset,on_delete=models.CASCADE,verbose_name='related Asset')
    status = models.IntegerField(default=0,choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.tracker_name


class Location(models.Model):
    tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE,verbose_name='related tracker')
    lat = models.DecimalField('Tracker latitude value',max_digits=8,decimal_places=4)
    lng = models.DecimalField('Tracker longitude value',max_digits=8,decimal_places=4)

    def __str__(self):
        return  self.tracker.tracker.asset_name


class Job(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='related user')
    tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE,verbose_name='related tracker')
    title = models.CharField('Job Title',max_length=150)
    origin = models.CharField('Job Origin',max_length=150)
    destination = models.CharField('Job Destination',max_length=150)
    description = models.TextField()
    def __str__(self):
        return  self.title

class Notification(models.Model):
    user_sender=models.ForeignKey(User,null=True,blank=True,related_name='user_sender',on_delete=models.CASCADE)
    user_revoker=models.ForeignKey(User,null=True,blank=True,related_name='user_revoker',on_delete=models.CASCADE)
    status=models.CharField(max_length=264,null=True,blank=True,default="unread")
    type_of_notification=models.CharField(max_length=264,null=True,blank=True)