from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib import messages
import cloudinary
import cloudinary_storage
import cloudinary.api
import cloudinary.uploader

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
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

    'apps.galeria.apps.GaleriaConfig',
    'apps.usuarios.apps.UsuariosConfig',
    'apps.financiamento.apps.FinanciamentoConfig',
    'formtools',
    'axes',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware'
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#MEDIA

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# MESSAGES
MESSAGE_TAGS = {
    messages.ERROR: 'danger', # REFERS TO BOOTSTRAP ALERT CLASS
    messages.SUCCESS: 'success',
    messages.INFO: 'warning',
}

# AXES
AXES_FAILURE_LIMIT = 5  # Número máximo de tentativas de login permitidas antes do bloqueio
AXES_COOLOFF_TIME = 1  # Tempo de bloqueio em horas (por exemplo, 1 hora)
AXES_LOCKOUT_CALLABLE = 'axes.handlers.default.lockout'
# AXES_LOCKOUT_TEMPLATE = 'lockout.html'  # Página personalizada para exibir quando o usuário é bloqueado

#CLOUDINARY
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': str(os.getenv('CLOUD_NAME')),
    'API_KEY': str(os.getenv('API_KEY')),
    'API_SECRET': str(os.getenv('API_SECRET')),
    'MEDIA_TAG': 'media',
    'STATIC_TAG': 'static',
}

# Configurar armazenamento de mídia
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# (Opcional) Configurar armazenamento estático
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'