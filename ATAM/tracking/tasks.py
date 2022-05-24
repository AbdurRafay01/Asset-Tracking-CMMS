
from celery import shared_task

from tracking.models import Location,Tracker, Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core import serializers
import json 


channel_layer = get_channel_layer()


@shared_task
def  get_location():
    tracker_location = {}
    tracker_id_list = []
    t_trackers = (Tracker.objects.all().values_list('id',flat=True))
    for i in range(len(t_trackers)):
        tracker_id_list.append((t_trackers[i]))
    try:
        print(tracker_id_list)
        for i in range(len(tracker_id_list)):
            print(tracker_id_list[i])
            obj=(Location.objects.filter(tracker=(tracker_id_list[i])).values('lat','lng').order_by('-id')[0])
            tracker1 = float(obj['lat']),float(obj['lng'])
            print(tracker1)
            tracker_location[(tracker_id_list[i])]=tracker1
        
    except:
        print("databases empty")
    async_to_sync(channel_layer.group_send)('location',{
        'type':'send_location',
        'text':json.dumps(tracker_location)
    })
    
@shared_task
def get_notification():
    
    status = Notification.objects.all()
    status_json = serializers.serialize('json', status)
    channel_layer = get_channel_layer()
    message = {
        'type': 'loc_message',
        'message': status_json 
    }
    async_to_sync(channel_layer.group_send)('core-realtime-data', message)