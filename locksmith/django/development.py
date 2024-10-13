from locksmith.env import env
from .base import *

DATABASES = {
    "default": {
        "ENGINE": env.str("DJANGO_DB_DEFAULT_ENGINE"),
        "NAME": env.str("DJANGO_DB_DEFAULT_NAME"),
        "USER": env.str("DJANGO_DB_DEFAULT_USER"),
        "PASSWORD": env.str("DJANGO_DB_DEFAULT_PASSWORD"),
        "HOST": env.str("DJANGO_DB_DEFAULT_HOST"),
        "PORT": env.str("DJANGO_DB_DEFAULT_PORT"),
        "OPTIONS": {
            "pool": False,
        },
    }
}

DEBUG = True
