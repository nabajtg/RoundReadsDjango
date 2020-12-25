import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'pi9g-nn-nzkqn6cgpzwgcy_%$c&e*nx&)dfk=nrm#z@6k5uq7='

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'corsheaders',
    'authentications',
    'books',
    'blogs',
    'djangotoolbox',
    
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'round_reads.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'round_reads.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        "NAME": 'round_reads_database',
        "HOST": 'mongodb+srv://booksystem:booksystem123@cluster0.ggvx7.mongodb.net/round_reads_database?retryWrites=true&w=majority',
        "USER": 'booksystem',
        "PASSWORD": 'booksystem123',
        
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": 'round_reads_database',
           "host": 'mongodb+srv://booksystem:booksystem123@cluster0.ggvx7.mongodb.net/round_reads_database?retryWrites=true&w=majority',
           "username": 'booksystem',
           "password": 'booksystem123',
           "authMechanism": 'SCRAM-SHA-1',
        }, 
    }
}



EMAIL_USE_TLS=True
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER='booksystem007@gmail.com'
EMAIL_HOST_PASSWORD='ncvgrwydkkyqonxc'
EMAIL_PORT=587


AUTH_USER_MODEL = 'authentications.CustomUser'

CORS_ORIGIN_ALLOW_ALL = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),  
     
}

DJOSER = {
    'LOGIN_FIELD' : 'email',
    'USER_CREATE_PASSWORD_RETYPE' : True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' : True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND' : True,
    'SEND_CONFIRMATION_EMAIL' : True,
    'SET_PASSWORD_RETYPE' : True,
    'ACTIVATION_URL' : 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL' : True,
    'SERIALIZERS' :{
        'user_create' : 'authentications.serializers.UserCreateSerializer',
        'user' : 'authentications.serializers.UserCreateSerializer',
        'user_delete' : 'djoser.serializers.UserDeleteSerializer',
    },
    
}


SIMPLE_JWT = {
    'USER_ID_FIELD': 'email',
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'AUTH_HEADER_TYPES': ('JWT',),
    
}
