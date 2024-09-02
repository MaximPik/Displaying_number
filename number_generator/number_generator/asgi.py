"""
ASGI config for number_generator project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from main.consumers import RandomNumberConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'number_generator.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/random-number/', RandomNumberConsumer.as_asgi()),
        ])
    ),
})
