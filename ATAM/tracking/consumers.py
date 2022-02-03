
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
    @database_sync_to_async
    def Data(self):
        tracker_dict = {}
        tracker = len(Tracker.objects.all())
        self.no_of_tracker = tracker
        for i in range(tracker):
            i+=1
            try:
                obj=(Location.objects.filter(tracker=(i+3)).values('lat','lng').order_by('-id')[0])
                tracker_dict[i]=obj
            except:
                print("databases empty")
        #print(tracker_dict)
        return tracker_dict
        
    #  for i in range(1000):
    #          await self.send(json.dumps({'lat':round(uniform(24.9180,25.1123),4),'lng':round(uniform(67.0971,67.3211),4)}))
    #          await sleep(3)
    #     self.close()

    # def Real_time_data(self):
    #     while True:
    #         #obj= Model.objects.filter(testfield=12).order_by('-id')[0]
    #         pass

# from channels.db import database_sync_to_async

# async def connect(self):
#     self.username = await self.get_name()

# @database_sync_to_async
# def get_name(self):
#     return User.objects.all()[0].name