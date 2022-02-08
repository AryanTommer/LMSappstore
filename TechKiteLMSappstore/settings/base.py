"""
Django settings for TechKiteLMSappstore project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from os.path import dirname, abspath, join, pardir, realpath

from django.conf.global_settings import LANGUAGES

BASE_DIR = realpath(join(dirname(dirname(abspath(__file__))), pardir))

INSTALLED_APPS = [
    'TechKiteLMSappstore.core.apps.CoreConfig',
    'TechKiteLMSappstore.api.apps.ApiConfig',
    'TechKiteLMSappstore.user.apps.UserConfig',
    'TechKiteLMSappstore.certificate.apps.CertificateConfig',
    'TechKiteLMSappstore.scaffolding.apps.ScaffoldingConfig',
    'parler',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'snowpenguin.django.recaptcha2',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'csp.middleware.CSPMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'TechKiteLMSappstore.urls'

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

WSGI_APPLICATION = 'TechKiteLMSappstore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': join(BASE_DIR, 'test.sqlite3'),
        }
    }
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'app_upload': '100/day',
        'app_register': '100/day',
    }
}

SITE_ID = 1

# Allauth configuration
# http://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = \
    'TechKiteLMSappstore.user.forms.SignupFormRecaptcha'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
PASSWORD_RESET_TIMEOUT_DAYS = 1
ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'TechKiteLMSappstore.user.forms.CustomResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EXCLUDED_LANGS = ('en-au', 'en-gb')
LANGUAGES = [lang for lang in LANGUAGES if lang[0] not in EXCLUDED_LANGS]
PARLER_LANGUAGES = {
    1: [{'code': code} for code, trans in LANGUAGES],
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_ROOT = join(BASE_DIR, 'media')
STATIC_ROOT = join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# if None will use the /tmp for downloading app release
RELEASE_DOWNLOAD_ROOT = None

# Default security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'if-none-match',
)
CORS_EXPOSE_HEADERS = (
    'etag',
    'x-content-type-options',
    'content-type',
)
CSP_DEFAULT_SRC = ('\'none\'',)
CSP_IMG_SRC = ('*',)
CSP_FONT_SRC = ('\'self\'',)
CSP_SCRIPT_SRC = ('\'self\'',)
CSP_CONNECT_SRC = ('\'self\'',)
CSP_STYLE_SRC = ('\'self\'',)
CSP_FORM_ACTION = ('\'self\'',)

CSP_SIGNUP = {
    'SCRIPT_SRC': ['https://google.com/recaptcha/',
                   'https://www.gstatic.com/recaptcha/'],
    'FRAME_SRC': ['https://www.google.com/recaptcha/'],
    'STYLE_SRC': '\'unsafe-inline\'',
}

# use modern no Captcha reCaptcha
NOCAPTCHA = True

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'

LOG_LEVEL = 'WARNING'
LOG_FILE = join(BASE_DIR, 'appstore.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}
LOCALE_PATHS = (
    join(BASE_DIR, 'locale/'),
)

# Disable in order for cooldown periods to work properly
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False

# App Store specific configs

# minimum number of comments to calculate a rating
RATING_THRESHOLD = 5

# number of days to include from today in the recent ratings calculation
RATING_RECENT_DAY_RANGE = 90

# for testing app uploads without cert validation set to false
VALIDATE_CERTIFICATES = True

# certification hash algorithm
CERTIFICATE_DIGEST = 'sha512'

# app archive downloader configuration
MAX_DOWNLOAD_FILE_SIZE = 1024 ** 2  # bytes
MAX_DOWNLOAD_TIMEOUT = 60  # seconds
MAX_DOWNLOAD_REDIRECTS = 10
MAX_DOWNLOAD_SIZE = 30 * (1024 ** 2)  # bytes
ARCHIVE_FOLDER_BLACKLIST = {
    'No .git directories': r'\.git$'
}

# certificate location configuration
TechKiteLMS_CERTIFICATE_LOCATION = join(
    BASE_DIR, 'TechKiteLMSappstore/certificate/TechKiteLMS.crt')
TechKiteLMS_CRL_LOCATION = join(
    BASE_DIR, 'TechKiteLMSappstore/certificate/TechKiteLMS.crl')

# whitelist for serializing markdown
MARKDOWN_ALLOWED_TAGS = [
    'audio', 'video', 'source', 'dt', 'dd', 'dl', 'table', 'caption', 'tr',
    'th', 'td', 'tbody', 'thead', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong',
    'em', 'code', 'pre', 'blockquote', 'p', 'ul', 'li', 'ol', 'br', 'del', 'a',
    'img', 'figure', 'figcaption', 'cite', 'time', 'abbr', 'iframe', 'q', ]
MARKDOWN_ALLOWED_ATTRIBUTES = {
    'audio': ['controls', 'src'],
    'video': ['poster', 'controls', 'height', 'width', 'src'],
    'source': ['src', 'type'],
    'a': ['href'],
    'img': ['src', 'title', 'alt'],
    'time': ['datetime'],
    'abbr': ['title'],
    'iframe': ['width', 'height', 'frameborder', 'src', 'allowfullscreen'],
    'q': ['cite'],
}

# Discourse configuration for creating categories automatically for newly
# registered apps
DISCOURSE_URL = 'https://help.TechKiteLMS.com'
DISCOURSE_USER = None
DISCOURSE_TOKEN = None
DISCOURSE_PARENT_CATEGORY_ID = 26

# list of values that will override or add user defined values for usage in
# templates; first key is the TechKiteLMS version for which the app is generated
APP_SCAFFOLDING_PROFILES = {}

# GitHub api configuration
GITHUB_API_BASE_URL = 'https://api.github.com'
GITHUB_API_TOKEN = None

# TechKiteLMS Email
TechKiteLMS_FROM_EMAIL = 'appstore@TechKiteLMS.com'
TechKiteLMS_INTEGRATIONS_APPROVAL_EMAILS = ['marketing-team@TechKiteLMS.com']