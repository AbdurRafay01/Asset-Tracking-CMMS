import imp
from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    # obj=(Location.objects.filter(tracker='1').values('lat','lng').order_by('-id')[0])
    # print(obj)
    # print(obj['lat'])
    # print(obj['lng'])
    return render(request,'tracking/index2.html')

def tracker_current_location(request,tracker_id):
    location = Location.objects.filter(tracker=(tracker_id)).values('lat','lng').order_by('-id')[0]
    data = {
        "tracker_id":tracker_id,
         "current_location" : location
         }
    return JsonResponse(data)