from unicodedata import name
from django.urls import path
from .views import*
app_name = 'tracking'
urlpatterns = [
    path('',index,name='index'),
    path('current_location/<int:tracker_id>',location_detail,name="current_location"),
    path('tracker/<int:tracker_id>',tracker,name="tracker"),
    path('current_location',location_list,name="current_location_list"),
    path('settings',setting,name="settings"),
    path("notification_alert/", notification_alert, name="notification_alert"),
    path("notification/", notification, name="notification"),
]
