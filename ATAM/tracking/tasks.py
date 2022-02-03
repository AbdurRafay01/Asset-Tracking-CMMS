
from .models import Location , Tracker
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


tracker_dict = {}
data = {}
counter = 0
@shared_task
def get_location():
    global tracker_dict
    global data
    global counter
    tracker = len(Tracker.objects.all())
    no_of_tracker = tracker
    for i in range(tracker):
        i+=1
        print(i)
        obj=(Location.objects.filter(tracker=i).values('lat','lng').order_by('-id')[0])
        tracker_dict[i]=obj
    obj =tracker_dict
    print(obj)
    #print(counter)
    if counter == 0:
        print("counter zero ")
        for i in range(no_of_tracker):
            i+=1
            tracker1 = float(obj[i]['lat']),float(obj[i]['lng'])
            print(tracker1)  
            data[i]=tracker1
            location= data
            try:
                async_to_sync(channel_layer.group_send('tracking',{'type':'send_location', 'location':location}))
                print("sending sucessfull......")
            except:
                 print("Failed......")

    else:
        #print("counter >1")
        for i in range(no_of_tracker):
            i+=1
            #print(data[i])
            tracker1 = float(obj[i]['lat']),float(obj[i]['lng'])
            if (data[i]) == (tracker1):
                print("skipping same value ......")
            else:
                print("sending.....")   
                data[i]=tracker1
                location ={i:{'lat':data[i][0],'lng':data[i][1]}}
                print(location)
                # try:
                #     print("sending sucessfull")
                #     async_to_sync(channel_layer.group_send)('tracking',{'type':'send_location','text':location})             
                # except:
                #     print("faileddddddd")

            #print("incrementing counter")
            counter+=1
            #print(counter)    





