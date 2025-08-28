# celery.py

import os
from celery import Celery
from django.conf import settings

env = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('Salesforce_API')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
