import json
import os
import random
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from pathlib import Path
from .services import data_producer

class DataWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'data_websocket_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        # await self.send(text_data=json.dumps({
        #     'message':"hello fellas"
        # }))


    async def disconnect(self, code):
        #await self.channel_layer.groupd_discard(self.group_name, self.channel_name)
        pass
        

    async def receive(self, text_data=None, bytes_data=None):
        print("the new data been received")
        data = json.loads(text_data)['message']
        print(data)


    async def send_message(self, message):
        print("=============message received from other process =============")
        # DATA_DIR = Path(__file__).resolve().parent.parent
        # datapath = os.path.join(DATA_DIR, "data", "todos.json")
        # with open(datapath, 'r') as file:
        #     data = json.load(file)
        #todo_user = data[random.randint(0, len(data))]

        todo_user = data_producer()
    
        # Send the message to the WebSocket
        print("ready to send message to client")
        await self.send(text_data=json.dumps({
            'message':todo_user
        }))



