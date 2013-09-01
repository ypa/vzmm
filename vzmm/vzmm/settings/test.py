from base import *
from os import environ

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vzmm-test',
        'USER': environ.get('DB_USER', None),
        'PASSWORD': environ.get('DB_PWD', None),
        'HOST': environ.get('DB_HOST', None),
        'PORT': '5432',
    }
}

MEDIA_URL = 'https://s3.amazonaws.com/vzmm-assets/'