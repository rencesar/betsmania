import os

import dj_database_url

from . import dirs

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(dirs.PROJECT_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] =  dj_database_url.config()

DATABASES['default']['ENGINE'] = 'django_postgrespool'