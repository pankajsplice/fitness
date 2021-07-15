# # Database
# # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
import pymysql
pymysql.install_as_MySQLdb()
ALLOWED_HOSTS = ['gofit.keycorp.in']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gofit',
        'USER': 'admin',
        'PASSWORD': '@dm!9098)(*',
        'HOST': '209.126.86.200',
        'PORT': '',
    }
}
