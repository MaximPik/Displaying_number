import asyncio
import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.send_random_number()

        while True:
            number = random.randint(1, 100)
            await self.send(json.dumps({'number': number}))
            await asyncio.sleep(5)

    async def disconnect(self, close_code):
        pass

    async def send_random_number(self):
        while True:
            number = random.randint(1, 100)
            await self.send(json.dumps({'number': number}))
            await asyncio.sleep(5)