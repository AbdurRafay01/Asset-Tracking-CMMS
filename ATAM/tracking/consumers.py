
import imp
from traceback import print_tb
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint , uniform
from asyncio import sleep
from .models import Location
from channels.db import database_sync_to_async
class WSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        
        while self.connect :
            obj = await self.Data()
            lat = float(obj['lat'])
            lng = float(obj['lng'])
            await self.send(json.dumps({'lat':lat,'lng':lng}))
            await sleep(30)
            obj2 = await self.Data()
            lat2 = float(obj2['lat'])
            lng2= float(obj2['lng'])
            if (lat + lng) == (lat2+lng2):
                print("same value agai")
            else :
                await self.send(json.dumps({'lat':lat2,'lng':lng2}))
                print("alag value ayi")
                obj =obj2

            
        self.close
    @database_sync_to_async
    def Data(self):
        obj=(Location.objects.values('lat','lng').order_by('-id')[0])
        return obj
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