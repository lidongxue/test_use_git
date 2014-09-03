from base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.' + 'sqlite3' if 'test' in sys.argv else 'mysql', 
        'NAME': 'Cord',
        'USER': 'jiazb',                      # Not used with sqlite3.
        'PASSWORD': 'jiazhaobing',             # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3308',                      # Set to empty string for default. Not used with sqlite3.
    },
    'slave_read': {
        'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.' + 'sqlite3' if 'test' in sys.argv else 'mysql', 
        'NAME': 'Cord',
        'USER': 'jiazb',
        'PASSWORD': 'jiazhaobing',
        'HOST': 'localhost',
        'PORT': '3308',
    },
    'payment': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payment',
        'USER': 'jiazb',
        'PASSWORD': 'jiazhaobing',
        'HOST': 'localhost',
        'PORT': '3308',
    },
}
ENABLE_ADMIN = True
STATIC_BASE_URL = 'http://cmstest.tvxio.com'
# celery settings
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8080/solr'
PAYMENT_ISMARTV_NOTIFY_URL = 'http://cmstest.tvxio.com/api/order/ismartv_notify/'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s -- %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': 'http://108774db938e45e2af84dae613ff52a4:b1730c0122884076add4cc04b87da9ed@sentry.tvxio.com/6',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console',],
            'level': 'WARN',
            'propagate': True,
        },
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

RAVEN_CONFIG = {
        'dsn': 'http://108774db938e45e2af84dae613ff52a4:b1730c0122884076add4cc04b87da9ed@sentry.tvxio.com/6',
    'register_signals': True,
}


# account settings
PAYMENT_EVTID = "1"
PAYMENT_APPID = "1002"
PAYMENT_ENABLED = True
PAYMENT_RELATE_COUNT = 3
PAYMENT_NOTIFY_URL = 'http://cmstest.tvxio.com/api/order/lenovo_notify/'

PAYMENT_ISMARTV_APPID = '1'
PAYMENT_ISMARTV_EVTID = '1'
PAYMENT_ISMARTV_NOTIFY_URL = 'http://cmstest.tvxio.com/api/order/ismartv_notify/'

HAYSTACK_SOLR_URL = 'http://cms_solr:8080/solr'

ENABLE_ADAPTIVE = False
ENABLE_EXPENSE_CLIP = True
IGNORE_PAYMENT_NOTIFY = True
CREATE_QRCODE_URL = "http://pay.t.tvxio.com/api/payment/order/create/"


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ['^core\.fields\.CrossDBForeignKey'])
add_introspection_rules([], ['^core\.fields\.CrossDBGenericForeignKey'])
add_introspection_rules([], ['^cord\.core\.fields\.TagsField'])
add_introspection_rules([], ['^cord\.core\.fields\.RatingField'])
add_introspection_rules([], ['^cord\.core\.fields\.CountingField'])


try:
    from celeryconfig import *
except ImportError, exp:
    pass

import djcelery
djcelery.setup_loader()
