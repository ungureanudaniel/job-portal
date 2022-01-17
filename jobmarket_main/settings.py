from pathlib import Path
import os
from django.conf import settings
from dotenv import load_dotenv

load_dotenv(verbose=True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', 'dincolo.eu', 'www.dincolo.eu']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'crispy_forms',
    'captcha',
    'debug_toolbar',
    'django_filters',
    'django_countries',
    'django.contrib.sites',
    'users',
    'recruiters',
    'candidates',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jobmarket_main.urls'

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

WSGI_APPLICATION = 'jobmarket_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Development Database
if (os.environ.get('DJANGO_DEV') == 'True'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# Production database
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = 'login'
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, "static/js", "serviceworker.js")
#--------------------EMAIL BACKEND SETTINGS----------------------------------
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
# EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
FROM_EMAIL = 'contact@dincolo.eu'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
CRISPY_TEMPLATE_PACK = 'bootstrap4'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#-------------------PROGRESSIVE WEB APP SETUP-----------------------------------
# PWA_APP_NAME = 'Dincolo'
# PWA_APP_DESCRIPTION = "Job portal PWA"
# PWA_APP_THEME_COLOR = '#000000'
# PWA_APP_BACKGROUND_COLOR = '#ffffff'
# PWA_APP_DISPLAY = 'standalone'
# PWA_APP_SCOPE = '/'
# PWA_APP_ORIENTATION = 'any'
# PWA_APP_START_URL = ''
# PWA_APP_STATUS_BAR_COLOR = 'default'
# PWA_APP_ICONS = [
#     {
#         'src': 'static/images/1200px-Flag_of_Romania.svg.png',
#         'sizes': '160x160'
#     }
# ]
# PWA_APP_ICONS_APPLE = [
#     {
#         'src': 'static/images/1200px-Flag_of_Romania.svg.png',
#         'sizes': '160x160'
#     }
# ]
# PWA_APP_SPLASH_SCREEN = [
#     {
#         'src': 'static/images/1200px-Flag_of_Romania.svg.png',
#         'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
#     }
# ]
# PWA_APP_DIR = 'ltr'
# PWA_APP_LANG = 'en-US'
