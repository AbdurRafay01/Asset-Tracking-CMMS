
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync

class TrackingConsumer(AsyncWebsocketConsumer):    
    async def connect(self):
        await self.channel_layer.group_add('tracking',self.channel_name)
        self.accept()
        print("-----------connection sucssesfulll")
    async def disconnect(self,close_code):
        print("-------------disconnecting--------")
        await self.channel_layer.group_discard('tracking',self.channel_name) 
        
    async def send_location(self,event):
        print("---------------sending location----------")
        location = event["location"]
        print("location agai ha",location)
        #await self.send(location)
        

        
    