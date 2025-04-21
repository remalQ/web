import os
from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (для продакшн-среды его нужно хранить в безопасности)
SECRET_KEY = 'your-secret-key-here'

# Настройки для шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Путь для глобальных шаблонов проекта
        ],
        'APP_DIRS': True,  # Включает поиск шаблонов в папках приложений
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

# Включаем статику и медиа
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Путь к дополнительным статикам в проекте
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Для сборки статики в продакшн

# Медиа-файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# База данных и другие настройки
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'showroom',
]

# Настройки для хостов
ALLOWED_HOSTS = ['*']  # Замените на список разрешенных хостов для продакшн-среды

# Среда для работы
DEBUG = True  # Включите в False для продакшн-среды

# Местоположение для логов
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Настройки времени
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
