from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
import random
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def generate_random_number():
    channel_layer = get_channel_layer()
    random_number = random.randint(0, 100)  # Генерация случайного числа
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