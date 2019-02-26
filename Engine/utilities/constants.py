import os

# Environment Definition ------------------------------------------------------------------------------
ENVIRONMENT = 'Local'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Env Related Variables  ------------------------------------------------------------------------------
if ENVIRONMENT == 'Local':
    DEBUG_EMAILER_LIST = ''

    # SQLLite Config
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    '''
     # MySQL Config
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'dblocal',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }

     # PostGRES Config
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.psycopg2',
             'NAME': 'dblocal',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
    
    '''

# Error Messages  ------------------------------------------------------------------------------------
'''
Suggested Error Code > 400, 401, 402 (Authorisation Violation Attempt)
                     > 500, 501, 502 (Server Processing Error)
                     > 600, 601, 602 (Database Error)
                     > 700, 701, 702 (Email Error)
'''

ERR_INVALID_REQUEST_TYPE = {
    'payload': {},
    'code': 400,
    'message': 'Invalid Payload Type'
}

ERR_INVALID_CONTEXT = {
    'payload': {},
    'code': 401,
    'message': 'Invalid Context'
}

ERR_PROCESS_FAILED = {
    'payload': {},
    'code': 500,
    'message': 'The requested task has failed! Please try again later'
}
