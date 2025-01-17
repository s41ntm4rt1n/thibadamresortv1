
from pathlib import Path
import environ
env=environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY=env('SECRET_KEY')

DEBUG = True

# ALLOWED_HOSTS = ['www.thibadamresort.org', 'thibadamresort.org']

DJANGO_APPS =[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = [
   'home',
   
]+DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thibadamresort.urls'

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
                'home.context_processors.contact',
                'home.context_processors.newsletter_subscription_form',
                'home.context_processors.room_checker_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'thibadamresort.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_DIRS = (
    BASE_DIR / 'static', 
)
STATIC_ROOT =  BASE_DIR / 'assets'
MEDIA_ROOT =  BASE_DIR / 'media' 
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
TIME_ZONE = 'Africa/Nairobi'

EMAIL_BACKEND = 'zoho_zeptomail.backend.zeptomail_backend.ZohoZeptoMailEmailBackend'
ZOHO_ZEPTOMAIL_HOSTED_REGION=env('ZOHO_ZEPTOMAIL_HOSTED_REGION')
ZOHO_ZEPTOMAIL_API_KEY_TOKEN=env('ZOHO_ZEPTOMAIL_API_KEY_TOKEN')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL =env('EMAIL_HOST_USER')  # if you don't already have this in settings
SERVER_EMAIL = env('EMAIL_HOST_USER') # ditto (default from-email for Django errors)
ADMIN_EMAIL='info@thibadamresort.org'
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')


# CLOUDFLARE_R2_BUCKET=env('CLOUDFLARE_R2_BUCKET')
# CLOUDFLARE_R2_BUCKET_ENDPOINT=env('CLOUDFLARE_R2_BUCKET_ENDPOINT')
# CLOUDFLARE_R2_ACCESS_KEY=env('CLOUDFLARE_R2_ACCESS_KEY')
# CLOUDFLARE_R2_SECRET_KEY=env('CLOUDFLARE_R2_SECRET_KEY')

# CLOUDFLARE_R2_STATIC_CONFIG_OPTIONS = {
#     "bucket_name": CLOUDFLARE_R2_BUCKET,
#     "default_acl": "public-read", 
#     "signature_version": "s3v4",
#     "endpoint_url": CLOUDFLARE_R2_BUCKET_ENDPOINT,
#     "access_key": CLOUDFLARE_R2_ACCESS_KEY,
#     "secret_key": CLOUDFLARE_R2_SECRET_KEY,
#     "location": "static",
# }

# CLOUDFLARE_R2_MEDIA_CONFIG_OPTIONS = {
#     "bucket_name": CLOUDFLARE_R2_BUCKET,
#     "default_acl": "public-read", 
#     "signature_version": "s3v4",
#     "endpoint_url": CLOUDFLARE_R2_BUCKET_ENDPOINT,
#     "access_key": CLOUDFLARE_R2_ACCESS_KEY,
#     "secret_key": CLOUDFLARE_R2_SECRET_KEY,
#     "location": "media",
# }

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": CLOUDFLARE_R2_MEDIA_CONFIG_OPTIONS,
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#         "OPTIONS": CLOUDFLARE_R2_STATIC_CONFIG_OPTIONS,
#     },
# }
