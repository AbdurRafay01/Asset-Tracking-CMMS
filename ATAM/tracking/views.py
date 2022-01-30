from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    # obj=(Location.objects.filter(tracker='1').values('lat','lng').order_by('-id')[0])
    # print(obj)
    # print(obj['lat'])
    # print(obj['lng'])

    
   
    return render(request,'tracking/index.html')