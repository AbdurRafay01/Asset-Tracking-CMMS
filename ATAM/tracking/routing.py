from django.urls import path
from .consumers import AllLocation,TrackerLocation
ws_urlpatterns = [
    path('current_location/',AllLocation.as_asgi()),
    path('current_location/tracker/<int:tracker_id>',TrackerLocation.as_asgi()),

    #path('stories/notification_testing/',NotificationConsumer.as_asgi())
]