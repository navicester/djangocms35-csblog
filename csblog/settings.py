# -*- coding: utf-8 -*-
import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for csblog project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e+o#0agm)7u5h7ouv73tmgc^0np5vfjml#b-ws#ygv=2ged31@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition





ROOT_URLCONF = 'csblog.urls'




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/



TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False # otherwise admin will report error


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'csblog', 'static'),
    # os.path.join(os.path.dirname(BASE_DIR), 'env', 'Lib', 'site-packages', 'djangocms_comments', \
    #     'boilerplates','bootstrap3','static'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'csblog', 'templates'),
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'site-packages-update', 'djangocms_comments', 'templates'),
                os.path.join(BASE_DIR, 'site-packages-update', 'tracking', 'templates'),
                # os.path.join(BASE_DIR, 'env', 'Lib', 'site-packages', 'mptt', 'templates'),
                ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]



INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages', 
    'cms',
    'menus',
    'sekizai',
    'treebeard', 
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',    
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_column',	
    'csblog',
    'serials',
    'textcourse',
    'plugin',
    'crispy_forms',

    'mptt',   
    
    # you will probably need to add these
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    # 'aldryn_boilerplates',   

    'aldryn_background_image',
    'aldryn_bootstrap3',
    'bootstrap3', # library django-bootstrap3, dependency of aldryn_bootstrap3

    # 'aldryn_style',  # duplicate name with djangocms_style

    # 'django_forms_bootstrap', # for {% load bootstrap3 %}, why is it OK now ?

    'djangocms_comments',
    # 'djangocms_inline_comment'  # not used finnally

	'markdown_deux',
    'djangocms_markdown', 
	
    # 'django_markwhat',    
    # 'cmsplugin_markdown', # Markdown-2.6.11 django-markwhat-1.6.0

    'hitcount',
    'tracking',
    'tracking2',
    # 'crispy_forms',

    'pagination',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github', 
    'allauth.socialaccount.providers.weixin', 

)

SITE_ID = 1

MIDDLEWARE = (
    'tracking.middleware.BannedIPMiddleware',
    'tracking2.middleware.VisitorTrackingMiddleware',    
    
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'pagination.middleware.PaginationMiddleware',   

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

    'tracking.middleware.VisitorTrackingMiddleware',
    'tracking.middleware.VisitorCleanUpMiddleware',    

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    
)


# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

# ALDRYN_BOILERPLATE_NAME = 'bootstrap3'


LANGUAGE_CHINESE_SIMPLE = 'zh'
LANGUAGE_CODE = LANGUAGE_CHINESE_SIMPLE

LANGUAGES = (
    ## Customize this
    # ('en', gettext('English')),
    (LANGUAGE_CHINESE_SIMPLE, gettext('Simplified Chinese')),

)


CMS_LANGUAGES = {
    # Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': LANGUAGE_CHINESE_SIMPLE,
            'hide_untranslated': False,
            'name': gettext('zh'),
            # 'name': gettext('Simplified Chinese'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('fullwidth.html', 'Fullwidth'),    
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': os.path.join(BASE_DIR, 'project1.db'),
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}


import socket
import os

db_server = os.getenv('DJANGO_SQL_SERVER')

MEDIA_PREFIX = None

DB_ORACLE = False
DB_MYSQL = False
DB_SQLITE = True

if "Oracle" == db_server:
    DB_ORACLE = True
    MEDIA_PREFIX = "DB_ORACLE_" + socket.gethostname()
elif "MySQL" == db_server: 
    DB_MYSQL = True
    MEDIA_PREFIX = "DB_SQL_" + socket.gethostname()   
elif "SQLite" == db_server:    
    DB_SQLITE = True
    MEDIA_PREFIX = "DB_SQLITE"
else:
    DB_SQLITE = True
    MEDIA_PREFIX = "DB_SQLITE"

print "is DB_MYSQL ? {}".format(DB_MYSQL)
if DB_MYSQL:
    DATABASES = {
        'default': {
            'CONN_MAX_AGE': 0,
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'localhost',
            'NAME': 'codingsoho',
            'PASSWORD': '123',
            'PORT': '',
            'USER': 'root'
        }
    }

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

# markdown_deux.conf.settings will import this file, it import reversely, someting wrong with the value
# from markdown_deux.conf.settings import MARKDOWN_DEUX_DEFAULT_STYLE
import re

MARKDOWN_DEUX_STYLES = {
    # "default": MARKDOWN_DEUX_DEFAULT_STYLE,
    "trusted": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": False,
    },
    # Here is what http://code.activestate.com/recipes/ currently uses.
    "recipe": {
        # "extras": {
        #     "code-friendly": None,
        # },
        # "safe_mode": "escape",
        "link_patterns": [
            # Transform "Recipe 123" in a link.
            (re.compile(r"recipe\s+#?(\d+)\b", re.I),
             r"http://code.activestate.com/recipes/\1/"),
        ],
        "extras": {
            "code-friendly": None,
            "pyshell": None,
            "header-ids": None, # show id for header
            "demote-headers": 2, # (origin 3), # starting from 3
            # "tag-friendly" : None, # for header
            "link-patterns": None,
            # `class` attribute put on `pre` tags to enable using
            # <http://code.google.com/p/google-code-prettify/> for syntax
            # highlighting.
            "html-classes": {"pre": "prettyprint"},
            "cuddled-lists": None,
            "footnotes": None,            
            # "fenced-code-blocks" : {'cssclass': 'mycodehilite', "prestyles":"background-color: #d2dee8;"},
            "fenced-code-blocks" : {'cssclass': 'mycodehilite',},
            "tables": 'mytable',            
        },
        "safe_mode": "escape",

    }
}

# needed for django-hitcount to function properly
SESSION_SAVE_EVERY_REQUEST = True

ALDRYN_NEWSBLOG_UPDATE_SEARCH_DATA_ON_SAVE = True
ALDRYN_NEWSBLOG_SEARCH = True

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# allauth BACKENDS
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
 
# LOGIN_REDIRECT_URL = "/accounts/profile/"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_EMAIL_REQUIRED = True # True. False
ACCOUNT_EMAIL_VERIFICATION = 'optional' # 'mandatory', 'optional', None

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# ACCOUNT_LOGOUT_ON_GET = False

EMAIL_HOST = "smtp.sina.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "hebinn2004@sina.com"
try:
    from setting_security import EMAIL_HOST_PASSWORD
except:
    EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
# EMAIL_USE_SSL 和 EMAIL_USE_TLS 是互斥的，即只能有一个为 True。
EMAIL_FROM = "hebinn2004@sina.com"
DEFAULT_FROM_EMAIL = "Django 学堂 <hebinn2004@sina.com>"


SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
    'weixin': {
        # 'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize',  # for media platform    
        # 'SCOPE': ['snsapi_base'],
        
        'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize',        
        'SCOPE': ['snsapi_userinfo'],

        # 'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/qrconnect',
        # 'SCOPE': ['snsapi_login'],
    },    
}