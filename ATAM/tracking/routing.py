
from django.urls import path
from .consumers import TrackingConsumer
ws_urlpatterns = [
    path('ws/tracking/',TrackingConsumer.as_asgi())
]