from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tracking.models import *

# Create your models here.
class Maintenance(models.Model):
    # tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE,verbose_name='related tracker')
    tracker = models.IntegerField()
    total_distance = models.DecimalField('Total Distance Covered',max_digits=8,decimal_places=4)
    description = models.CharField(default="NO MAINTENANCE SCHEDULE",max_length=100)
    maintenance_status = models.CharField(default="Not Pending", max_length=15)
    maintenance_limit = models.IntegerField(default=20, validators=[ MaxValueValidator(100), MinValueValidator(20)])
    def __int__(self):
        return  self.tracker
