"""
Django settings for plxk project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$6j3t72_h9(&5cyli92srv8sz^injngq$!nf=3+de=7_b33y&b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Мої налаштування ---------
STAS_DEBUG = False
DEV_PLACE = 'Home'  # Home або Work, це впливає на підключення до бд
# --------------------------

ALLOWED_HOSTS = ['10.10.10.0/24']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'googlecharts',
    'qsstats',
    'widget_tweaks',
    'webpack_loader',

    'accounts',
    'bets',
    'boards',
    'crm',
    'docs',
    'correspondence',
    'gi',
    'polls',
    'tickets',
    'edms',
]

MIDDLEWARE_CLASSES = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plxk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'plxk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DEV_PLACE == 'Work':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'plxk',
            'USER': 'root',
            'PASSWORD': 'Cvjhjlbyf11',
            'HOST': '10.10.10.22',  # Or an IP Address that your DB is hosted on
            'PORT': '3306',
            'ATOMIC_REQUESTS': True,
        },

        'lite': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'fb_test': {
            'ENGINE': 'firebird',
            'NAME': 'E:/db/lis.fdb',  # Path to database or db alias
            'USER': 'SYSDBA',  # Your db user
            'PASSWORD': 'Cvjhjlbyf11',  # db user password
            'HOST': '10.10.10.8',  # Your host machine
            'PORT': '3050',  # If is empty, use default 3050
            'OPTIONS': {'charset': 'win1251'}
        },
        'fb1': {
            'ENGINE': 'firebird',
            'NAME': 'E:/db/lis.fdb',  # Path to database or db alias
            'USER': 'SYSDBA',  # Your db user
            'PASSWORD': 'masterke',  # db user password
            'HOST': '10.10.10.7',  # Your host machine
            'PORT': '3050',  # If is empty, use default 3050
            'OPTIONS': {'charset': 'win1251'}
        },
    }
elif DEV_PLACE == 'Home':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PLXK',
            'USER': 'root',
            'PASSWORD': 'Cvjhjlbyf11',
            'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
            'PORT': '3306',
            'ATOMIC_REQUESTS': True,
        },
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True  # підтримка часових поясів


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')

MEDIA_URL = '/media/'

LOGOUT_REDIRECT_URL = 'home'

LOGIN_REDIRECT_URL = 'home'

# FILE_UPLOAD_HANDLERS = [
#     'django.core.files.uploadhandler.TemporaryFileUploadHandler',
# ]