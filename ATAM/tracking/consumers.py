
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class TrackingConsumer(WebsocketConsumer):    
    def connect(self):
        async_to_sync( self.channel_layer.group_add('tracking',self.channel_name))
        self.accept()

    def disconnect(self):
        async_to_sync( self.channel_layer.group_add('tracking',self.channel_name))
        
    async def send_location(self,event):
        location = event["text"]
        await self.send(json.dumps(location))
        

        
    