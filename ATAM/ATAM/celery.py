import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ATAM.settings')

app = Celery('ATAM')
app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
    'get_location_30s':{

      'task':'tracking.tasks.get_location',
      'schedule' :30.0 
    },
    'get_notification_10s' : {
      'task': 'tracking.tasks.get_notification',
      'schedule': 10.0
    }
}


app.autodiscover_tasks()
