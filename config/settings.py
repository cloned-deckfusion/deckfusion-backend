# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import dj_database_url

from decouple import config
from pathlib import Path


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ENVIRONMENT
# └─────────────────────────────────────────────────────────────────────────────────────

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set secret key
SECRET_KEY = config("BACKEND_SECRET_KEY", cast=str, default="") or "secret-key"

# Define environment constants
LOCAL = "local"
STAGING = "staging"
PRODUCTION = "production"

# Retrieve environment from .env
ENVIRONMENT = config("BACKEND_ENVIRONMENT", default=PRODUCTION)

# Retrieve debug from .env
DEBUG = config("BACKEND_DEBUG", cast=bool, default=False) and ENVIRONMENT != PRODUCTION

# Determine whether to enable Django Admin
ENABLE_DJANGO_ADMIN = config("BACKEND_ENABLE_DJANGO_ADMIN", cast=bool, default=True)

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ NETWORK
# └─────────────────────────────────────────────────────────────────────────────────────

# Define allowed hosts
ALLOWED_HOSTS = str(config("BACKEND_ALLOWED_HOSTS", cast=str, default="")).split(",")

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SERVER
# └─────────────────────────────────────────────────────────────────────────────────────

# Define root URL config
ROOT_URLCONF = "config.urls"

# Configure ASGI application
ASGI_APPLICATION = "config.asgi.application"

# Configure WSGI application
WSGI_APPLICATION = "config.wsgi.application"

# Define CORS allowed origins
CORS_ALLOWED_ORIGINS = [
    h.strip() for h in config("BACKEND_CORS_ALLOWED_ORIGINS", default="").split(",")
]
CORS_ALLOWED_ORIGINS = [i for i in CORS_ALLOWED_ORIGINS if i]

# Check if staging or production
if ENVIRONMENT in [STAGING, PRODUCTION]:
    # Enforce https
    SECURE_SSL_REDIRECT = True

    # Enforce HTTP Strict Transport Security (1 year)
    SECURE_HSTS_SECONDS = 31536000

    # Configure https header (needed for Heroku)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Needed for Heroku

    # Enforce secure cookies
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTALLED APPS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define installed apps
INSTALLED_APPS = [
    # Django Contrib
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Django Extensions
    "django_extensions",
    # Django REST Framework
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "dynamic_rest",
    # Django Celery Beat
    "django_celery_beat",
    # Channels
    "channels",
    # Project
    "user",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ MIDDLEWARE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEMPLATES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define templates
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
            "debug": DEBUG,
        },
    },
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DATABASE
# └─────────────────────────────────────────────────────────────────────────────────────

# Get remote database URL
database_url = str(config("DATABASE_URL", ""))

# Check if remote database URL is defined
if database_url:

    # Define lifetime of a database connection
    conn_max_age = config("DATABASE_CONN_MAX_AGE", cast=int, default=500)

    # Define databases
    DATABASES = {
        "default": dj_database_url.parse(
            database_url, conn_max_age=conn_max_age, ssl_require=True
        )
    }

# Otherwise, handle case of local database
else:

    # Get database credentials
    database_engine = "django.db.backends.postgresql_psycopg2"
    database_name = config("BACKEND_DATABASE_NAME", default="dalpha")
    database_user = config("BACKEND_DATABASE_USER", default="postgres")
    database_password = config("BACKEND_DATABASE_PASSWORD", "postgres")
    database_host = config("BACKEND_DATABASE_HOST", default="backend_db")
    database_port = config("BACKEND_DATABASE_PORT", cast=int, default=5432)

    # Define databases
    DATABASES = {
        "default": {
            "ENGINE": database_engine,
            "NAME": database_name,
            "USER": database_user,
            "PASSWORD": database_password,
            "HOST": database_host,
            "PORT": database_port,
        }
    }

# Set default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ AUTHENTICATION
# └─────────────────────────────────────────────────────────────────────────────────────

# Set custom user model
AUTH_USER_MODEL = "user.User"

# Define password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
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

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STATIC FILES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define static URL
STATIC_URL = config("BACKEND_STATIC_URL", cast=str, default="") or "/static/"

# Define static root
STATIC_ROOT = BASE_DIR / "staticfiles"

# Define static files directories
STATICFILES_DIRS = [BASE_DIR / "static"]

# Define static files storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INTERNATIONALIZATION
# └─────────────────────────────────────────────────────────────────────────────────────

# Define language code
LANGUAGE_CODE = "en-us"

# Define time zone
TIME_ZONE = "UTC"

# Define whether to use timezone aware datetimes
USE_TZ = False

# Define whether to enable translations
USE_I18N = True

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK
# └─────────────────────────────────────────────────────────────────────────────────────

# Append slash
APPEND_SLASH = False

# Define Django REST framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# Determine whether to enable browsable API
ENABLE_BROWSABLE_API = config("BACKEND_ENABLE_BROWSABLE_API", cast=bool, default=True)

# Check if browsable API is enabled
if ENABLE_BROWSABLE_API:

    # Add session authentication
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].extend(
        [
            "rest_framework.authentication.SessionAuthentication",
        ]
    )

    # Add form parser classes
    REST_FRAMEWORK["DEFAULT_PARSER_CLASSES"].extend(
        [
            "rest_framework.parsers.FormParser",
            "rest_framework.parsers.MultiPartParser",
        ]
    )

    # Add browsable API renderer
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].extend(
        [
            "dynamic_rest.renderers.DynamicBrowsableAPIRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ]
    )

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ REDIS
# └─────────────────────────────────────────────────────────────────────────────────────

# Retrieve Redis URL from .env
REDIS_URL = config("REDIS_URL", default="redis://redis:6379/0")

# Set Redis broker settings
BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY
# └─────────────────────────────────────────────────────────────────────────────────────

# Define Celery URLs
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_BROKER_URL = REDIS_URL

# Define Celery beat scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Set Celery always eager setting
CELERY_ALWAYS_EAGER = config("CELERY_ALWAYS_EAGER", cast=bool, default=False)

# Define Celery timezone
CELERY_TIMEZONE = "UTC"

# Ensure broker connection retries on startup
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
