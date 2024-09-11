import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from .sheduler import random_number_storage
from django.contrib.auth.models import AnonymousUser

class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'] == AnonymousUser(): #Проверка на анонима
            await self.close()
        elif self.scope['user'].is_authenticated:
            await self.channel_layer.group_add("random_numbers", self.channel_name)
            await self.accept()
            if random_number_storage.random_number is not None:
                await self.send(text_data=str(random_number_storage.random_number))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("random_numbers", self.channel_name)

    async def receive(self, text_data):
        pass

    async def send_random_number(self, event):
        random_number = event['number']
        await self.send(text_data=str(random_number))


async def generate_random_numbers():
    while True:
        random_number = random.randint(0, 100)
        await RandomNumberConsumer.channel_layer.group_send(
            "random_numbers",
            {
                "type": "send_random_number",
                "number": random_number
            }
        )
        await asyncio.sleep(5)
