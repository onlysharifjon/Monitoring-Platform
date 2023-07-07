import os
from pathlib import Path
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-psu^3vbi&xifinv=vc#@5*dgzb&=7e$irfoml40yumjy2bcno^'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor_uploader',
    'ckeditor',
    'NewsApp', 'QuizApp', 'rest_framework', 'corsheaders',
    'drf_yasg',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = default_headers + (
    'cache-control',
)

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

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

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_DefaultToolbarConfig': [

            {
                'name': 'format',
                'items': ['Styles', 'Format', 'Font', 'FontSize'],
            },
            {
                'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {
                'name': 'basic-styles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                          'Superscript', ],
            },
            {
                'name': 'templates',
                'items': ['Templates'],
            },
            {
                'name': 'paragraph',
                'items': ['NumberedList', 'BulletedList', 'Outdent', 'Indent',
                          'HorizontalRule', 'JustifyLeft', 'JustifyCenter',
                          'JustifyRight', 'JustifyBlock', ],
            },
            '/',
            {
                'name': 'action',
                'items': ['Undo', 'Redo']
            },
            {
                'name': 'extra',
                'items': ['Link', 'Unlink', 'Blockquote', 'Image', 'Table', 'Mathjax', 'CodeSnippet',
                          'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
            },
            {
                'name': 'source',
                'items': ['Source', 'Maximize', ],
            },

        ],
        'title': False,

        'toolbar': 'DefaultToolbarConfig',

        'format_tags': 'p;pre;h1;h2;h3;h4;h5;h6',

        'removeDialogTabs': ';'.join([
            'image:advanced',
            'image:Link',
            'link:upload',
            'table:advanced',
            'tableProperties:advanced',
        ]),
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,

        'height': '500',
        'width': '100%',
        'forcePasteAsPlainText ': True,

        'mathJaxClass': 'mathjax-latex',
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_SVG',
        'tabSpaces': 4,
        'extraPlugins': 'mathjax, codesnippet',

        'codeSnippet_theme': 'pojoaque',
        'codeSnippet_languages': {
            'python': 'Python',
            'cpp': 'C++',
            'java': 'Java'
        },
    }
}
