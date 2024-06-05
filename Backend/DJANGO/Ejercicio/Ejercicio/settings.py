from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6_zv&e)r)pi1=df4a(+7en91*vlzzv9n6^$*po^udnd!ewxf=#'

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.1#IniciarSesion/static',
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.2#Registro/static',
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.3#RecuperarContra/static',
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.3#RecuperarContra/static',
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.5#TerminosCondiciones/static',
    'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/2.1#Panelnicio/static',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ejercicio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.1#IniciarSesion',
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.2#Registro',
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.3#RecuperarContra',
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.4#RecuperarContra2',
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/1.5#TerminosCondiciones',
            'C:/Users/Andres Gordillo/Desktop/utp/2024/LabSoft/Vetpet-Final/Backend/DJANGO/Ejercicio/Ejercicio/templates/2.1#Panelnicio',
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

WSGI_APPLICATION = 'Ejercicio.wsgi.application'

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
