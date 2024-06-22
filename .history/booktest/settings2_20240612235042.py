ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'bookms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# mysql数据库需要自己定义
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookms',		# 数据库的名字
        'USER': 'root',		        # 登录数据库的用户名
        'PASSWORD': '123456',	    # 登录数据库的密码
        'HOST': '127.0.0.1',	    # 数据库的IP地址
        'PORT': '3306',		        # 数据库的端口
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

