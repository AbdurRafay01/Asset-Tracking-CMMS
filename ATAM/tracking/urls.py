from unicodedata import name
from django.urls import path
from .views import*
app_name = 'tracking'
urlpatterns = [
    path('',index,name='index'),
    path('current_location/<int:tracker_id>',location_detail,name="current_location"),
    path('current_location',location_list,name="current_location_list")
]