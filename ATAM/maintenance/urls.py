from django.urls import path
from .views import *

app_name = 'maintenance'
urlpatterns = [
    path('',index,name='index'),
    path('<int:tracker_iD>', update_limit ,name='update_limit'),
    # path('<int:tracker_iD>',trackerdetail,name="trackerdetail"),
    path('driver/<int:tracker_iD>',driver,name="driver"),
    path('driver/reset_status/<int:tracker_iD>',reset_status,name="reset_status"),
]