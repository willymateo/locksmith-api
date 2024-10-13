"""
Django settings for locksmith project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os

from locksmith.env import BASE_DIR, env


env.read_env(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "passwords.apps.PasswordsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "locksmith.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "locksmith.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DJANGO_DB_DEFAULT_ENGINE"),
        "NAME": env.str("DJANGO_DB_DEFAULT_NAME"),
        "USER": env.str("DJANGO_DB_DEFAULT_USER"),
        "PASSWORD": env.str("DJANGO_DB_DEFAULT_PASSWORD"),
        "HOST": env.str("DJANGO_DB_DEFAULT_HOST"),
        "PORT": env.str("DJANGO_DB_DEFAULT_PORT"),
        "OPTIONS": {
            "pool": {
                # https://www.psycopg.org/psycopg3/docs/api/pool.html#module-psycopg_pool
                "min_size": env.int("DJANGO_DB_DEFAULT_POOL_MIN_SIZE"),
                "max_size": env.int("DJANGO_DB_DEFAULT_POOL_MAX_SIZE"),
                "name": env.str("DJANGO_DB_DEFAULT_POOL_NAME"),
                "timeout": env.float("DJANGO_DB_DEFAULT_POOL_TIMEOUT"),
                "max_waiting": env.int("DJANGO_DB_DEFAULT_POOL_MAX_WAITING"),
                "max_lifetime": env.float("DJANGO_DB_DEFAULT_POOL_MAX_LIFETIME"),
                "max_idle": env.float("DJANGO_DB_DEFAULT_POOL_MAX_IDLE"),
                "reconnect_timeout": env.float(
                    "DJANGO_DB_DEFAULT_POOL_RECONNECT_TIMEOUT"
                ),
                "num_workers": env.int("DJANGO_DB_DEFAULT_POOL_NUM_WORKERS"),
            },
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = True

from locksmith.app_settings.cors import *