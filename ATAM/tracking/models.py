from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    phone_number=models.IntegerField(default=0,null=False,help_text="Number format:0300-1234567")
    