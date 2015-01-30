"""
Django settings for vacationator project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('VACATIONATOR_SECRET_KEY', 'a0b1@)o)u(2nh5j@9r78bgr8=pnx3wvx#ts8fpr^b3vcd#ue9+')

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
    'tracker',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vacationator.urls'

WSGI_APPLICATION = 'vacationator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap3.backends.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_URI = os.environ.get('VACATIONATOR_LDAP_URI', 'ldap://127.0.0.1')
AUTH_LDAP_BASE_DN = os.environ.get('VACATIONATOR_LDAP_BASE_DN',
                                   'dc=example,dc=com')

AUTH_LDAP_BIND_TEMPLATE = os.environ.get('VACATIONATOR_LDAP_BIND_TEMPLATE',
                                         '{username}@example.com')
AUTH_LDAP_UID_ATTRIB = os.environ.get("VACATIONATOR_LDAP_UID_ATTRIB", 'uid')
AUTH_LDAP_ADMIN_GROUP = os.environ.get("VACATIONATOR_LDAP_ADMIN_GROUP",
                                       "CN=Admin,dc=example,dc=com")

