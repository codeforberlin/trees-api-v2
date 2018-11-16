SECRET_KEY = 'this is not a very secret key'

DEBUG = False

ALLOWED_HOSTS = ['localhost']

# USE_X_FORWARDED_HOST = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BASE_URL = '/api/v2/'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'trees_api',
    }
}
