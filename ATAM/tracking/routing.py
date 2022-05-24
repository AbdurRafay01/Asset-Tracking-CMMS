from django.urls import path
from .consumers import AllLocation,TrackerLocation, Notification_Alert
ws_urlpatterns = [
    path('current_location/',AllLocation.as_asgi()),
    path('current_location/tracker/<int:tracker_id>',TrackerLocation.as_asgi()),
    path('notification_alert/', Notification_Alert.as_asgi()),
]