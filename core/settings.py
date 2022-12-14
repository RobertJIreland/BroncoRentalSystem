#IMPORTS
import os
from pathlib import Path

#BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET KEY
SECRET_KEY = '^imyfuo7z!%$s=(jhzvzz#4o3y@p29aeqk3$+9tjmvwfet@+zq'

#DEBUG - TRUE IN PRODUCTION - FALSE IN DEPLOYMENT
DEBUG = True

#ALLOWED HOSTS
ALLOWED_HOSTS = ['0.0.0.0','192.168.1.160', '127.0.0.1', '54.157.215.171', 'bronco-rental-system-env.eba-pjymga2b.us-east-1.elasticbeanstalk.com']


#INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'whitenoise',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'core',
    'car_rental_system',
    'api', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build')
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#PASSWORD VALIDATION
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


#META INFORMATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

DATETIME_FORMAT="Y-m-d H:i"

USE_I18N = True

USE_L10N = False

USE_TZ = False

#STATIC FILES
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


#LOGIN
LOGIN_REDIRECT_URL = 'main-home'
LOGIN_URL = 'login'

#EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'broncoscarrentalsystem@gmail.com'
EMAIL_HOST_PASSWORD = 'CarRentalPassword'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]


