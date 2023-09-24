# celery.py
import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')

app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process_broadcast_task': {
        'task': 'broadcasts.tasks.process_broadcast',
        'schedule': crontab(minute=00, hour=8),
    },
}

app.conf.timezone = 'UTC'
