from .base import *


import dj_database_url # postgre db_url


# turn debug to false in production
DEBUG = True

# installed apps for prod only
INSTALLED_APPS += [

]

# read secret key from environment variable
SECRET_KEY = os.environ.get("SECRET_KEY")


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# redirect all non secure requests to https
SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# set to use postgres backend in production
DATABASES['default'] = dj_database_url.parse( os.environ.get("DATABASE_URL"),
                                                 conn_max_age=600)