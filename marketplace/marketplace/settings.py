from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT

"""
Django settings for marketplace project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", default=env('SECRET_KEY'))

DEBUG = int(os.environ.get("DEBUG", default=1))

ALLOWED_HOSTS=['127.0.0.1', 'localhost', 'testserver']
if os.environ.get("HOME") == '/root':
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'sorl.thumbnail',
    'django.contrib.postgres',
    'ckeditor',
    'ckeditor_uploader',
    'django_apscheduler',
    'django_celery_results',
    'channels',
    'django.contrib.sitemaps',
    'rest_framework',
    'django_filters',
    'main.apps.MainConfig',
    'chat.apps.ChatConfig',
    'api.apps.ApiConfig',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'main.middleware.MobileMiddleware',
]

ROOT_URLCONF = 'marketplace.urls'


DESKTOP_TEMPLATE_DIRS = (
    '/main/templates',
)
MOBILE_TEMPLATE_DIRS = (
    '/main/mobile_templates',
) + DESKTOP_TEMPLATE_DIRS

TEMPLATE_DIRS = DESKTOP_TEMPLATE_DIRS


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
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

WSGI_APPLICATION = 'marketplace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if os.environ.get("HOME") == '/root':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        }
    }


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

REDIS_HOST = '127.0.0.1'
if os.environ.get("HOME") == '/root':
    REDIS_HOST = 'redis'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://' + REDIS_HOST + ':6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Конфигурация Channels
ASGI_APPLICATION = 'marketplace.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(REDIS_HOST, 6379)],
        },
    },
}

EMAIL_FILE_PATH = '.'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
      'log_formatter': {
          'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
          'style': '{',
      }
    },
    'handlers': {
        'django_all': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'log.log',
            'formatter': 'log_formatter'
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
            'include_html': True,
        }
    },
    'loggers': {
        'main': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django_all'],
            'level': 'WARNING',
        },
        'django': {
            'handlers': ['django_all'],
            'level': 'WARNING',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
        },
        'django.db.backends': {
            'handlers': ['django_all'],
            'level': 'WARNING',
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = 'register'
LOGIN_REDIRECT_URL = '/'

CKEDITOR_UPLOAD_PATH = "uploads/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# Celery Configuration Options
CELERY_REDIS_HOST = 'localhost'
if os.environ.get("HOME") == '/root':
    CELERY_REDIS_HOST = 'redis'

CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_URL = 'redis://' + CELERY_REDIS_HOST + ':6379'
CELERY_BROKER_TRNASPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + CELERY_REDIS_HOST + ':6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACKS_LATE = True

# Custom settings
ADMIN_EMAIL = 'admin@marketplace.ru'
DOMAIN_NAME = 'http://127.0.0.1:8000/'

VONAGE_KEY = env('VONAGE_KEY')
VONAGE_SECRET = env('VONAGE_SECRET')

if os.environ.get("HOME") == '/root':
    VONAGE_KEY = os.environ.get("VONAGE_KEY")
    VONAGE_SECRET = os.environ.get("VONAGE_SECRET")

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}