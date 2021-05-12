from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['192.168.43.40', '127.0.0.1', 'exp://127.0.0.1:19000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False
# DEFAULT_FROM_EMAIL = 'PocketStack@outlook.com'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eagleofnile27@gmail.com'
EMAIL_HOST_PASSWORD = '813046902499324752912246469'


CORS_ORIGIN_ALLOW_ALL = True


LOGIN_URL = '/redirect-to-app'


# ACCOUNT_ADAPTER = 'users.adapter.MyAccountAdapter'