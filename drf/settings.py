
import os
from pathlib import Path
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Make sure to get the SECRET_KEY from an environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-mv&us85d-2@*q#c58#skz34toi9kl-7qph2(h%a26drf-!523i')

# Never deploy with Debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    # List your installed apps here
]

MIDDLEWARE = [
    # List your middleware here
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # List your context processors here
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
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
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add the React build directory to the STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'path_to_react_app/build/static'),
]

# Static files storage using WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Rest of your Django configuration...

# Add configuration for Django-Heroku at the end of your settings.py
try:
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    raise ImproperlyConfigured('django-heroku must be installed to use this settings configuration.')

# Rest of your Django configuration...
