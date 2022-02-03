import imp


import os 
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ATAM.settings')

app = Celery('ATAM')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
    'get_location30s':{
        'task': 'tracking.tasks.get_location',
        'schedule':30.0
    }
}

app.autodiscover_tasks()


