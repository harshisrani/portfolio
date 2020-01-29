"""
Django settings for myportfolio project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG")
DEBUG = False

# Here we define where our redis service is running
# REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
# REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
# REDIS_DJANGO_CACHE_DB = os.environ.get("REDIS_DJANGO_CACHE_DB", 5)
# REDIS_CELERY_DB = os.environ.get("REDIS_CELERY_DB", 2)

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "width": 1120,
    "cleanup_on_startup": True,
    "custom_undo_redo_levels": 20,
    "selector": "textarea",
    "theme": "modern",
    "plugins": """
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            """,
    "toolbar1": """
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            """,
    "toolbar2": """
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            """,
    "contextmenu": "formats | link image",
    "menubar": True,
    "statusbar": True,
}

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",
    "main",
    "tinymce",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myportfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myportfolio.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Cache time to live is 15 mn.
CACHE_TTL = 5 * 1

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://redis:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "example",
    }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myportfoliodb",
        "USER": "postgres",
        "PASSWORD": "postgres",
        # "HOST": "locahost",
        "HOST": "postgres",
        "PORT": 5432,
    }
}

# Celery configuration
# https://blog.syncano.rocks/configuring-running-django-celery-docker-containers-pt-1/


# Set Redis as Broker URL
BROKER_URL = f"redis://redis:6379/2"

# Set django-redis as celery result backend
CELERY_RESULT_BACKEND = "django-db"
CELERY_REDIS_MAX_CONNECTIONS = 1

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = False
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_TASK_RESULT_EXPIRES = 600

# configure queues, currently we have only one
# CELERY_DEFAULT_QUEUE = 'default'
# CELERY_QUEUES = (
#     Queue('default', Exchange('default'), routing_key='default'),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# image url on localhost
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "main/static"),
    # os.path.join(BASE_DIR, 'static'),
    # "/usr/local/lib/python3.7/site-packages/django/contrib/admin/static",
)


# Email parameters
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 10


# Configuration which writes all logging from the django logger to a local file
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "info.log",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
}
