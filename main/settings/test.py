import os

from . import dirs

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(dirs.PROJECT_DIR, 'db.sqlite3'),
    }
}