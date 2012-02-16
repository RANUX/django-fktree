# -*- coding: UTF-8 -*-
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#==============================================================================
# TESTS
#==============================================================================

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture',
             '--all-modules',
             '--nologcapture',
             '--verbosity=2',
             '--with-coverage',
             '--cover-package=fktree',
#             '--cover-html',
#             '--with-doctest',
             'fktree'
             #             '--cover-erase',
             #             '--cover-tests',
]

INSTALLED_APPS = (
    'fktree',
)