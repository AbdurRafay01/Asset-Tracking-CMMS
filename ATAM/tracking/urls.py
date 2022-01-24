from unicodedata import name
from django.urls import path
from .views import*
app_name = 'tracking'
urlpatterns = [
    path('',index,name='index')
]