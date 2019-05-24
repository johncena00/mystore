"""
Django settings for mystore project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku

from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd-q&@%oab++9=csw0fbdqfd$(-)xbn^awecbkg0%cw@&v2ub(a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'estore',
    'spgateway',
    'bootstrap4',
    'fontawesome',
    'anymail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'spgateway.middleware.SpgatewaySameSiteCookieMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'estore.middleware.cart.CartMiddleware',
]

ROOT_URLCONF = 'mystore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mystore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SPGATEWAY_PROFILE = {
    os.environ.get('SPGATEWAY_MERCHANT_ID', ''): {
        'MerchantID': os.environ.get('SPGATEWAY_MERCHANT_ID', ''),
        'HashKey': os.environ.get('SPGATEWAY_HASHKEY', ''),
        'HashIV': os.environ.get('SPGATEWAY_HASHIV', ''),
    }
}
SPGATEWAY_MERCHANTID = os.environ.get('SPGATEWAY_MERCHANT_ID', '')
SPGATEWAY_ORDERMODEL = 'estore.Order'

# Activate Django-Heroku.
django_heroku.settings(locals())

if os.environ.get('MAILGUN_API_KEY'):
    ANYMAIL = {
        'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_SENDER_DOMAIN'),
    }
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
elif DEBUG:
    INSTALLED_APPS += ('naomi',)
    EMAIL_BACKEND = 'naomi.mail.backends.naomi.NaomiBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'