from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%pahak=4m3aydm)$*d8(7in3w-4gy%za12mt-r**su8pts3b3r'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]
MIDDLEWARE = MIDDLEWARE +  [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = ("127.0.0.1")
try:
    from .local import *
except ImportError:
    pass
