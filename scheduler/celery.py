from __future__ import absolute_import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')

from django.conf import settings
from celery import Celery

app = Celery('scheduler')

# This reads, e.g., CELERY_ACCEPT_CONTENT = ['json'] from settings.py:
app.config_from_object('django.conf:settings', namespace='CELERY')

# For autodiscover_tasks to work, you must define your tasks in a file called 'tasks.py'.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# For print particular scheduled message
@app.task
def schedule_message(message):
	print (message)	