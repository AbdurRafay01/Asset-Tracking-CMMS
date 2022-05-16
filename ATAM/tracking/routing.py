import imp
from django.urls import path
from .consumers import WSConsumer,WSConsumerTracker
ws_urlpatterns = [
    path('ws/tracking/',WSConsumer.as_asgi()),
    path('ws/tracking/tracker/<int:tracker_id>',WSConsumerTracker.as_asgi())
]