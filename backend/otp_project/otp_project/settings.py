from pathlib import Path
import os
from dotenv import load_dotenv


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from backend folder
load_dotenv(BASE_DIR.parent / ".env")


# SECURITY SETTINGS
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []


# INSTALLED APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "corsheaders",

    # Local apps
    "accounts",
]


# MIDDLEWARE
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# CORS (allow React frontend)
CORS_ALLOW_ALL_ORIGINS = True


# ROOT URL
ROOT_URLCONF = "otp_project.urls"


# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = "otp_project.wsgi.application"


# DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# PASSWORD VALIDATION
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


# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# STATIC FILES
STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}


# EMAIL SETTINGS (loaded from .env)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# CUSTOM USER MODEL
AUTH_USER_MODEL = "accounts.User"