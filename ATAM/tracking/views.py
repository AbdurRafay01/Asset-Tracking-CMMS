import json
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

#for creating a rest api 
from rest_framework.response import Response
from rest_framework import status
from .serializers import LocationSerializer
from .models import Location
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.decorators import api_view   


# Create your views here.

def index(request):
    return render(request,'tracking/index.html')

def setting(request):
    return render(request,'tracking/settings.html')

def notification_alert(request):
    return render(request, 'tracking/tracker.html')

def tracker(request,tracker_id):
    current_location = Location.objects.filter(tracker=(tracker_id)).values('lat','lng').order_by('-id')[0]
    job = Job.objects.filter(tracker=(tracker_id)).values()
    context = {'current_location':current_location,'job':job}
    #data = current_location|job[0]
    #return JsonResponse(context)
    return render(request,'tracking/tracker.html',context)

@api_view(['GET', 'POST', 'DELETE'])
def location_detail(request,tracker_id):
    """
    Retrieve, update or delete a Location.
    """
    try:
        location = Location.objects.filter(tracker=(tracker_id)).only('lat','lng').order_by('-id')[0]
    except :

        return JsonResponse({"status": "error", "data": "No data found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    
    '''May be needed in future'''
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = LocationSerializer(location, data=data)
    #     #print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     Location.delete()
    #     return HttpResponse(status=204)
        

@api_view(['GET', 'POST', 'DELETE'])
def location_list(request):
    """
    Retrieve or post Locations.
    """
    try:
        locations = Location.objects.all()
        
    except :
        #print(location)
        return JsonResponse({"status": "error", "data": "No data found"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = LocationSerializer(locations, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        # 'safe=False' for objects serialization
        
    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        serializer = LocationSerializer(data=location_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
