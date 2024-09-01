from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/random-number/$', consumers.RandomNumberConsumer.as_asgi()),
]