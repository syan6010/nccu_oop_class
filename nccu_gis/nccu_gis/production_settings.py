# Import all default settings.
from .settings import *

import os
import dj_database_url

ON_HEROKU = os.environ.get('ON_HEROKU')
HEROKU_SERVER = os.environ.get('HEROKU_SERVER')

# 修復資料庫測試2
if ON_HEROKU:
    DATABASE_URL = 'postgresql://<postgresql>'
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}




# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = True