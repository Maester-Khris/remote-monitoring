from .wsconsumer import DataWebsocketConsumer
import asyncio

def send_socket_message():
    asyncio.run(DataWebsocketConsumer.send_message())