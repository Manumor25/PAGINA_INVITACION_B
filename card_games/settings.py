import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# 🔐 SEGURIDAD
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-key')

DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = [
    'pagina-invitacion-b-2.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',

    'pagina-invitacion-b-2.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]


# 🔹 REDIRECCIONES
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'


# 🔹 APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django.contrib.humanize',
    'crispy_forms',
    'crispy_bootstrap4',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# 🔹 MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'card_games.urls'
WSGI_APPLICATION = 'card_games.wsgi.application'


# 🔹 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# 🔹 DATABASE
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# 🔹 PASSWORDS
AUTH_PASSWORD_VALIDATORS = []


# 🌎 LOCALIZACIÓN
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'

USE_I18N = True
USE_TZ = True


# 🔹 STATIC FILES (clave para tu problema)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# 🔹 MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 🔹 DEFAULT PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'