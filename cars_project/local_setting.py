# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%4bm(%nw2n$(@n07j$-zpy55uq#7oxrbm&v)#6zzn$(=b98ky_'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Pa$$word'
    }
}
