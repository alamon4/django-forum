"""
Django settings for theHorton project.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
=======
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
<<<<<<< HEAD
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ui^0wrri_w7$su(i-h0s@wsanawe&k8xk2f__(gymw-&x%s)ik'
=======
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-_=2+76982ym9%z7o&9894gy%7dwhg2x1jfit!g)ku%zh+hodh'
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
=======
    'django.middleware.security.SecurityMiddleware',
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c
)

ROOT_URLCONF = 'theHorton.urls'

WSGI_APPLICATION = 'theHorton.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/topics/i18n/
=======
# https://docs.djangoproject.com/en/dev/topics/i18n/
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/howto/static-files/
=======
# https://docs.djangoproject.com/en/dev/howto/static-files/
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c

STATIC_URL = '/static/'
