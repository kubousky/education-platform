from .base import *

DEBUG = False

ADMINS = (
    ('Jakub Parcheta', 'jakub.parcheta@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'Ryszard1'
    }
}