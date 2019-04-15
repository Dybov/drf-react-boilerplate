from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c!ue7h1t(ui*aj@v3+s*fh7zz$o$56&7x9c4&9*@iqx@zwb=3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
