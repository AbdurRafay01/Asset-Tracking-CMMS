import imp
from django.urls import path
from .consumers import WSConsumer
ws_urlpatterns = [
    path('ws/tracking/',WSConsumer.as_asgi())
]