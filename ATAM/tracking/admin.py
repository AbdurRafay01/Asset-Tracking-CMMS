from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Tracker)
admin.site.register(Location)
admin.site.register(Asset)
admin.site.register(Job)
admin.site.register(Notification)