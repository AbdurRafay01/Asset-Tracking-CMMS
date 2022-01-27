
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint , uniform
from asyncio import sleep
class WSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        # self.Data()
        for i in range(1000):
             await self.send(json.dumps({'lat':round(uniform(24.9180,25.1123),4),'lng':round(uniform(67.0971,67.3211),4)}))
             await sleep(3)
        self.close
    # async def Data(self):
    #     for i in range(1000):
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