#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from optparse import OptionParser

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                },
            },
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
        ],
        INSTALLED_APPS=[
            'fktree',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
    )


from django_nose import NoseTestSuiteRunner

def runtests(*test_args, **kwargs):
    if not test_args:
        test_args = ['fktree']

    test_runner = NoseTestSuiteRunner(**kwargs)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)