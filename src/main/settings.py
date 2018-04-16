import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
REPO_ROOT = os.path.dirname(SRC_PATH)

DEBUG = True
DEBUGTOOLBAR_ENABLED = True
METRICS_ENABLED = False
CACHE_BACKEND = 'django.core.cache.backends.dummy.DummyCache'
CACHE_LOCATION = None

CACHE_PREFIX = 'katka_api'

SECRET_KEY = 'gj%hml#3z3*pgmzzpdm21tfh8#$bt_ad!@s5fekusv=jqefef('

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'main.urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG' if DEBUG else 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['console']
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/katka-api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',

    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# DATABASE DEFAULTS
DATABASES_ENGINE = 'django.db.backends.sqlite3'
DATABASES_NAME = 'db.sqlite'
DATABASES_OPTIONS = {}
DATABASES_TEST = {}
DATABASES_CONN_MAX_AGE = 0

SESSION_COOKIE_NAME = 'katka_api_sid'
CSRF_COOKIE_NAME = 'katka_api_csrftoken'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': DATABASES_ENGINE,
        'NAME': DATABASES_NAME,
        'OPTIONS': DATABASES_OPTIONS,
        'TEST': DATABASES_TEST,
        'CONN_MAX_AGE': DATABASES_CONN_MAX_AGE,
    }
}


# Caches
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'KEY_PREFIX': CACHE_PREFIX
    }
}

# Django Rest Framework
REST_FRAMEWORK = {
    # TODO 'EXCEPTION_HANDLER': 'exception_handler_name',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}
