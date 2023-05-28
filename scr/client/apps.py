# apps.py

from django.apps import AppConfig
from django.conf import settings
from celery import current_app


class YourAppConfig(AppConfig):
    name = 'client'

    def ready(self):
        # Регистрация задач Celery
        if 'celery' in settings.INSTALLED_APPS:
            current_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
