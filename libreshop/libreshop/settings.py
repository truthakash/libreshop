"""
Django settings for libreshop project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from . import patch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Detect whether or not we are in a testing mode.
TESTING = (sys.argv[1] if len(sys.argv) > 1 else None) in ['test', 'behave']

ALLOWED_HOSTS = []

# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # Use database-backed sessions.
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'behave_django',
    'social.apps.django_app.default',
    'oauth2_provider',
    'rest_framework',
    'nested_inline',
    'widget_tweaks',
)

LOCAL_APPS = (
    'api',
    'shop',
    'customers',
    'products',
    'inventory',
    'carts',
    'orders',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.github.GithubOAuth2',
    'social.backends.reddit.RedditOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('TWITTER_SECRET')

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

if TESTING:
    SOCIAL_AUTH_GITHUB_KEY = os.environ.get('GITHUB_LOCAL_KEY')
    SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('GITHUB_LOCAL_SECRET')
    SOCIAL_AUTH_REDDIT_KEY = os.environ.get('REDDIT_LOCAL_KEY')
    SOCIAL_AUTH_REDDIT_SECRET = os.environ.get('REDDIT_LOCAL_SECRET')
else:
    SOCIAL_AUTH_GITHUB_KEY = os.environ.get('GITHUB_DEV_KEY')
    SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('GITHUB_DEV_SECRET')
    SOCIAL_AUTH_REDDIT_KEY = os.environ.get('REDDIT_DEV_KEY')
    SOCIAL_AUTH_REDDIT_SECRET = os.environ.get('REDDIT_DEV_SECRET')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'libreshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'libreshop/templates'),],
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

WSGI_APPLICATION = 'libreshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Location to which `./manage.py collectstatic` will move files.
STATIC_ROOT = ''

# Serve project-wide static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'libreshop/static'),
)

# Set up logging.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] (%(levelname)s) %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple_yellow': {
            'format': ('\033[33m%s\033[0m' % # ANSI escape code for yellow.
                '[%(asctime)s] (%(levelname)s) %(name)s: %(message)s'),
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_yellow',
        },
    },
    'loggers': {
        'products': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'carts': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# Set up an in-memory email backend for development and testing.
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Declare the default `from` email.
DEFAULT_FROM_EMAIL = 'LibreShop <contact@libreshop.org>'
