
from itertools import count
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint , uniform
from asyncio import sleep
from .models import Location,Tracker
from channels.db import database_sync_to_async
class WSConsumer(AsyncWebsocketConsumer):
    no_of_tracker = 0;
    counter = 0
    data = {}
    async def connect(self):
        
        await self.accept()
        while self.connect :
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


class WSConsumerTracker(AsyncWebsocketConsumer):
    data = {}
    counter = 0
    async def connect(self):

        self.tracker_id =self.scope['url_route']['kwargs']['tracker_id']
        print(self.tracker_id)
        print(self.tracker_id)
        print("connected!")
        await self.accept()
        while self.connect :
            obj = await self.Data(self.tracker_id)
            if self.counter == 0 :   
                print(obj)    
                tracker1 = float(obj[1]['lat']),float(obj[1]['lng'])
                print(tracker1)  
                self.data[0]=tracker1
                await self.send(json.dumps(self.data,indent=4))
                await sleep(30)
            else:    
                print("counter >1") 
                print(self.data[0])
                tracker1 = float(obj[1]['lat']),float(obj[1]['lng'])
                if (self.data[0]) == (tracker1):
                    print("Same value as previous continue.....")
                else:
                    print("value is not same sending.....")   
                    self.data[0]=tracker1
                    await self.send(json.dumps(self.data,indent=4))
                    #await self.send(json.dumps({{'lat':self.data[i][0],'lng':self.data[i][1]}},indent=4))
                await sleep(30)             
            print("incrementing counter")
            self.counter+=1
            print(self.counter)            
        self.close
    
    @database_sync_to_async
    def Data(self,tracker_id):
        tracker_dict = {}
        #tracker = len(Tracker.objects.all())
        #self.no_of_tracker = tracker
        print("tracker id :",tracker_id)
        try:
            obj=(Location.objects.filter(tracker=(tracker_id)).values('lat','lng').order_by('-id')[0])
            tracker_dict[tracker_id]=obj
        except:
                print("databases empty")
        return tracker_dict