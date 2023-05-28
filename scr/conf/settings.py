from pathlib import Path
from django.urls import reverse_lazy
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_%fh0tk+eh!e#=8zwasw^qk3x4liau6*t2!099%-b))zo8uxeq'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # main
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    # apps
    'core',
    'authentication',
    'client',
    'organization',
    # install,
    'crispy_forms',
    'crispy_bootstrap4',
    'django_filters',
    'bootstrapform',
    'captcha',
]

SITE_ID = 1
AUTH_USER_MODEL = 'authentication.User'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ADMIN_TOOLS_THEMING_CSS = 'css/theming.css'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'artem',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': '1234'
    },
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher'
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = reverse_lazy('home')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RECAPTCHA_PUBLIC_KEY = '6Lf50v8kAAAAAPvQJ0hE7sZkKplSaa7EtTY0I4ZS'
RECAPTCHA_PRIVATE_KEY = '6Lf50v8kAAAAAIKE9hiNEBLZvKalh5vz5Od_f0dv'
#txzpwuoyqjwytmok
# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'arttyyom@gmail.com'
EMAIL_HOST_PASSWORD = 'txzpwuoyqjwytmok'

EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = ['arttyyom@yandex.ru']
# Включение поддержки Celery
# ...

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# ...

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# ...
from datetime import timedelta
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'check-conditions-every-second': {
        'task': 'core.tasks.check_order_conditions',
         'schedule': crontab(hour=0, minute=0),
    },
}

