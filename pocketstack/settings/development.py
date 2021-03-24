from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['192.168.43.40', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CORS_ORIGIN_ALLOW_ALL = True
