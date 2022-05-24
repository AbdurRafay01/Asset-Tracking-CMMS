
import asyncio
from itertools import count
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint , uniform
from asyncio import sleep
from .models import Location,Tracker,Notification,User
from channels.db import database_sync_to_async
import time

class Notification_Alert(AsyncWebsocketConsumer):
    notification_exist = False
    async def connect(self):
        await self.accept()
        while self.connect:
            obj = await self.Data()
            # sleep(10)
            if self.notification_exist:
                # print("Sending udpate to client about tracker notification")
                alert = {"status": 1}
                await self.send(json.dumps(alert, indent=4))
            else:
                alert = {"status": 0}
                await self.send(json.dumps(alert, indent=4))
                # print("no updates about region cross")
                
    async def disconnect(self, code):
        return await super().disconnect(code)

    #this function returns the latest notification from the database  
    @database_sync_to_async
    def Data(self):
        notifications = len(Notification.objects.all())
        self.notification_exist = notifications > 0
        return


class AllLocation(AsyncWebsocketConsumer):
    no_of_tracker = 0
    counter = 0
    data = {}
    async def connect(self):
        
        await self.accept()
        while self.connect:
            obj = await self.Data()
            print(obj)
            print(self.counter)
            if  self.counter == 0:
                print("counter zero ")
                for i in range(self.no_of_tracker):
                    i+=1
                    tracker1 = float(obj[i]['lat']),float(obj[i]['lng'])
                    print(tracker1)  
                    self.data[i]=tracker1
                await self.send(json.dumps(self.data,indent=4))
                await sleep(30)
            else:
                print("counter >1")
                for i in range(self.no_of_tracker):
                    i+=1
                    print(self.data[i])
                    tracker1 = float(obj[i]['lat']),float(obj[i]['lng'])
                    if (self.data[i]) == (tracker1):
                        print("value same not sending......")
        
                    else:
                        print("value is not same sending.....")   
                        self.data[i]=tracker1
                        await self.send(json.dumps({i:{'lat':self.data[i][0],'lng':self.data[i][1]}},indent=4))
                await sleep(30)             
            print("incrementing counter")
            self.counter+=1
            print(self.counter)            
        self.close
    #this function returns the latest location from database.    
    @database_sync_to_async
    def Data(self):
        tracker_dict = {}
        tracker = len(Tracker.objects.all())
        self.no_of_tracker = tracker
        for i in range(tracker):
            i+=1
            try:
                obj=(Location.objects.filter(tracker=(i)).values('lat','lng').order_by('-id')[0])
                tracker_dict[i]=obj
            except:
                print("databases empty")
        return tracker_dict


class TrackerLocation(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add('location',self.channel_name)
        self.tracker_id =self.scope['url_route']['kwargs']['tracker_id']
        self.data = {}
        await self.accept()

    async def disconnect(self,event):
        await self.channel_layer.group_discard('location',self.channel_name)
        print("Disconnected! ",event)
   
    async def send_location(self,event):
        location_data = json.loads(event['text']) 
        track_id = str(self.tracker_id)
        tracker_location = float(location_data[track_id][0]),float(location_data[track_id][1])
        
        if self.data:
            
            if self.data[0] == tracker_location:
                print("same location as previous pass......")
            else:
                print("different location then previous sending to front-end.....")   
                self.data[0]=tracker_location
                await self.send(json.dumps(self.data))
           
        else:
            #print("different location then previous sending to front-end.....")   
            self.data[0]=tracker_location
            await self.send(json.dumps(self.data))
            #await sleep(30)

            
    async def websocket_receive(self,event):
        print(event)
        data_to_get=json.loads(event['text'])
        print(data_to_get)
        user_to_get=await self.get_user(int(data_to_get))
        print(user_to_get)
        # RAFAY creating changes to website a/c to warning notification
        await self.create_notification(user_to_get)
#         self.room_group_name='test_consumer_group'
#         channel_layer=self.get_channel_layer()
#         await (channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 "type":"send_notification",
#                 "value":json.dumps(get_of)
#             }
# )
        print('receive',event)
    @database_sync_to_async
    def create_notification(self,receiver,typeof="Out of Region",status="unread"):
        notification_to_create=Notification.objects.create(user_revoker=receiver,type_of_notification=typeof)
        return (notification_to_create.user_revoker.username,notification_to_create.type_of_notification)
    
    @database_sync_to_async
    def get_user(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return "Unknown User"