# celery.py

import os
from celery import Celery

# Установка переменной окружения, указывающей Django-проект
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')

# Загрузка конфигурации из файла настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файла tasks.py в приложениях Django
app.autodiscover_tasks()
