from unicodedata import name
from django.urls import path
from .views import*
app_name = 'tracking'
urlpatterns = [
    path('',index,name='index'),
    path('current_location/<int:tracker_id>',tracker_current_location,name="current_location")
]