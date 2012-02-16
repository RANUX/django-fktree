#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from os.path import dirname, abspath
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = 'settings'
from django_nose.runner import NoseTestSuiteRunner


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def runtests(*test_args):
    if not test_args:
        test_args = ['fktree']

    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    try:
        def run_tests(test_args, verbosity, interactive):
            runner = NoseTestSuiteRunner(
                verbosity=verbosity,
                interactive=interactive,
                failfast=False
            )
            return runner.run_tests(test_args)
    except ImportError:
        # for Django versions that don't have DjangoTestSuiteRunner
        from django.test.simple import run_tests
    failures = run_tests(
        test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])