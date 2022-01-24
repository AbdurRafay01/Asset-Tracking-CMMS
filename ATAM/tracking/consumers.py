
from channels.generic.websocket import WebsocketConsumer
import json
from random import randint , uniform
from time import sleep
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(1000):
            self.send(json.dumps({'lat':round(uniform(24.9180,25.1123),4),'lng':round(uniform(67.0971,67.3211),4)}))
            sleep(30)

