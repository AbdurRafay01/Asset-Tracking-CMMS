
from channels.generic.websocket import WebsocketConsumer ,AsyncWebsocketConsumer
import json
from random import randint , uniform
from time import sleep
class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        self.Data()
        # for i in range(5):
        #     self.send(json.dumps({'lat':round(uniform(24.9180,25.1123),4),'lng':round(uniform(67.0971,67.3211),4)}))
        #     sleep(3)
        #self.close
    def Data(self):
        for i in range(1000):
             self.send(json.dumps({'lat':round(uniform(24.9180,25.1123),4),'lng':round(uniform(67.0971,67.3211),4)}))
             sleep(3)
        self.close()

    def Real_time_data(self):
        while True:
            #obj= Model.objects.filter(testfield=12).order_by('-id')[0]
            pass