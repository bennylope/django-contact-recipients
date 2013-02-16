import django

if django.VERSION[:2] >= (1, 3):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASE_ENGINE = 'sqlite3'


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'contact_recipients',
]


SECRET_KEY = "BusTransportingCarnivalCruisePassengersCrashesIntoSewageTreatmentPlant"
