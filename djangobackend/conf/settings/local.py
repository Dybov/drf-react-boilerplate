from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c!ue7h1t(ui*aj@v3+s*fh7zz$o$56&7x9c4&9*@iqx@zwb=3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Django-debug-toolbar requirements
INTERNAL_IPS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].insert(
    0,
    'rest_framework.renderers.BrowsableAPIRenderer'
)


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(
            WEBPACK_STATS_DIR, 'webpack-stats.dev.json'),
    }
}
