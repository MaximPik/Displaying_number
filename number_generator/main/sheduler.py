from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
import random
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class RandomNumberStorage:
    """Класс для хранения случайного числа"""
    def __init__(self):
        self.random_number = random.randint(0, 100)

    def generate_random_number(self):
        self.random_number = random.randint(0, 100)  # Генерация случайного числа
        return self.random_number

random_number_storage = RandomNumberStorage()

def generate_random_number():
    channel_layer = get_channel_layer()
    random_number = random_number_storage.generate_random_number()
    async_to_sync(channel_layer.group_send)(
        "random_numbers",
        {
            "type": "send_random_number",
            "number": random_number
        }
    )

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_random_number, 'interval', seconds=5)
    scheduler.start()