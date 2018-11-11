SECRET_KEY = 'this is not a very secret key'

DEBUG = False

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'trees_api',
    }
}
