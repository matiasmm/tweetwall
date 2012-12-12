#Example dev settings
from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='sqlite:////sqlite_db_path')}

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

STATIC_URL = '/static'

STATICFILES_DIRS = (
    'your_staticfiles_dirs',
    )

SECRET_KEY = 'YOUR_SECRET_KEY'

#For django-debug-toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INSTALLED_APPS += ('debug_toolbar',)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATE_DIRS = (
    'your_template_dirs',
    )

#Twitter credentials
CONSUMER_KEY = 'CONSUMER_KEY'

CONSUMER_SECRET = 'CONSUMER_SECRET'
