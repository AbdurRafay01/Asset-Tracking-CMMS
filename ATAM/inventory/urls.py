
from django.urls import path
from .views import*
app_name = 'inventory'
urlpatterns = [
    path('',index,name='index'),
    path('add_asset/', add_asset ,name='add_asset'),
    path('add_asset/<int:id>', update_asset ,name='add_asset_instance'),
    path('delete_asset/<int:id>', delete_asset ,name='delete_asset'),
    path('add_tracker/', add_tracker ,name='add_tracker'),
    path('add_tracker/<int:id>', update_tracker ,name='add_tracker_instance'),
    path('delete_tracker/<int:id>', delete_tracker ,name='delete_tracker'),
    
]