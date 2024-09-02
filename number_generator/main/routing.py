from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/random/', consumers.RandomNumberConsumer.as_asgi()),
]