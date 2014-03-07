import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'sftcelau#e_ei*#r*5^#_!cecu2+gr#(q+25_opp9os01e)0qn'
DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*',]

INSTALLED_APPS = (
    'tyler',
)

ROOT_URLCONF = 'tylerproj.urls'

WSGI_APPLICATION = 'tylerproj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from memcacheify import memcacheify

CACHES = memcacheify()
