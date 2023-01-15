import os

from .base import *  # noqa: F403

# ENVIRONMENT
DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY", "")
SITE_URL = os.environ.get("SITE_URL", "http://0.0.0.0:8000")

# HOSTS
ALLOWED_HOSTS = ["*"]

# STATIC ROOT
STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")  # noqa: F405

# MEDIA ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, "public", "media")  # noqa: F405

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(os.path.join(BASE_DIR, "db.sqlite3")),
    }
}
