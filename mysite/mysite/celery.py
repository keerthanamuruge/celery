import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# pass the project name in Celery(project_name)
app = Celery('mysite')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# # Load task modules from all registered Django apps.
app.autodiscover_tasks()


# Celery Beat Settings
app.conf.beat_schedule = {
    'celery_schedule_task': {
        'task': 'celery_projects.tasks.test_schedule',
        'schedule': crontab(hour=12, minute=30),
    }
}


#
#
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')