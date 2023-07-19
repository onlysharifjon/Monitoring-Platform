import os
from pathlib import Path
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-psu^3vbi&xifinv=vc#@5*dgzb&=7e$irfoml40yumjy2bcno^'

DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://quvonchbek.uz", "http://quvonchbek.uz"]

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
    'NewsApp', 'QuizApp', 'TeacherApp',
    'rest_framework', 'corsheaders',
    'drf_yasg',

]

REST_FRAMEWORK = {
    'DEFAULT_FORMATS': ['json'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

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

JAZZMIN_SETTINGS = {
    "site_title": "TATU Oliy Matematika Kafedrasi",
    "site_header": "Oliy Matematika",
    "site_brand": "Oliy Matematika",
    "site_icon": "images/favicon.png",
    # Add your own branding here
    "site_logo": None,
    "welcome_sign": "Salom, admin panelga xush kelibsiz!",
    # Copyright on the footer
    "copyright": "TUIT",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "/admin", "permissions": ["auth.view_user"]},
        {"name": "Yangiliklar", "url": "/admin/NewsApp", "permissions": ["auth.view_user"]},
        {"name": "O'qituvchilar", "url": "/admin/TeacherApp", "permissions": ["auth.view_user"]},
        {"name": "Testlar", "url": "/admin/QuizApp", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"name": "Redoc", "url": "redoc", "permissions": ["auth.view_user"]},
        {"name": "Swagger", "url": "swagger", "permissions": ["auth.view_user"]},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        "TeacherApp": "fas fa-user",
        "TeacherApp.Lesson": "fas fa-calendar",
        "TeacherApp.Teacher": "fas fa-user",
        "TeacherApp.Room": "fas fa-door-open",
        "TeacherApp.Subject": "fas fa-book",
        "TeacherApp.ForeignLangs": "fas fa-language",
        "TeacherApp.Group": "fas fa-users",
        "TeacherApp.ScientificDegree": "fas fa-flask",
        "TeacherApp.ScientificTitle": "fas fa-graduation-cap",

        "QuizApp": "fas fa-question",
        "QuizApp.Quiz": "fas fa-question",

        "NewsApp": "fas fa-envelope",
        "NewsApp.Blog": "fas fa-pen-nib"
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    # Related Modal #
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "vertical_tabs",
    # override change forms on a per modeladmin basis
    #     "changeform_format_overrides": {
    #         "auth.user": "vertical_tabs",
    #         # "auth.group": "vertical_tabs",
    #     },
}
