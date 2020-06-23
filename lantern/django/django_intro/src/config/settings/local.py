from .base import *  #noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_intro_local',
        'USER': 'django_intro',
        'PASSWORD': 'django_intro',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}
