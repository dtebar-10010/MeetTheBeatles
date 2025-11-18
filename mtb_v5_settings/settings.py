from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path( __file__ ).resolve( ).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^yhjhum@rt2o(@hzfm@m34oym5g9!$00j8*wd01a&ge^x_sy5e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ "localhost", "127.0.0.1" ]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )

STATICFILES_DIRS = [
os.path.join( BASE_DIR, 'static' ),
# ... other directories if needed
]

MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
MEDIA_URL = '/media/'

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'django_ckeditor_5',
'mtb_v5_app',
]

CKEDITOR_5_CONFIGS = {
'default': {
'toolbar'   : [
'heading', '|',
'bold', 'italic', 'underline', 'strikethrough', '|',
'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
'alignment', '|',
'bulletedList', 'numberedList', '|',
'outdent', 'indent', '|',
'link', 'blockQuote', '|',
'undo', 'redo'
],
'fontSize'  : {
'options': [ 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22 ]
},
'fontFamily': {
'options': [
'default',
'Arial, Helvetica, sans-serif',
'Courier New, Courier, monospace',
'Georgia, serif',
'Times New Roman, Times, serif',
]
},
'contentsCss': ['/static/css/ckeditor-custom.css', '/static/css/admin-ckeditor.css'],

},
}

# Add media path for uploads if needed
CKEDITOR_5_UPLOAD_PATH = "uploads/"
CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mtb_v5_settings.urls'

TEMPLATES = [
{
'BACKEND' : 'django.template.backends.django.DjangoTemplates',
'DIRS'    : [ BASE_DIR / 'templates' ],
'APP_DIRS': True,
'OPTIONS' : {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]

WSGI_APPLICATION = 'mtb_v5_settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME'  : BASE_DIR / 'db.sqlite3',
}
}

# DATABASES = {
#   'default': {
#     'ENGINE'  : 'django.db.backends.postgresql',  # Or 'django.db.backends.postgresql_psycopg2'
#     'NAME'    : 'mtb_v4_pgdb',
#     'USER'    : 'postgres',
#     'PASSWORD': 'postgres',
#     'HOST'    : 'localhost',  # Or the IP address of your PostgreSQL server
#     'PORT'    : '5432',
#   }
# }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CRISPY_TEMPLATE_PACK = 'uni_form'
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"
# CRISPY_TEMPLATE_PACK = "bootstrap3"

# email configuration settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dtebar@gmail.com'
# EMAIL_HOST_PASSWORD = 'gaml xvnn vaar nyvy'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'dtebar@top-quarks.com'

# email configuration settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dtebar@gmail.com'
# EMAIL_HOST_PASSWORD = 'qjjw mcay bqgi vvbt'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'dtebar@top-quarks.com'
