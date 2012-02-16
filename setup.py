# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import sys



VERSION = (1, 0, 0)
README_FILE = 'README.rst'

__version__ = '.'.join((str(each) for each in VERSION[:4]))
__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


try:
    long_description = open(README_FILE).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
                     "``long_description`` (%s)\n" % README_FILE)
    sys.exit(1)

setup(name='django-fktree',
    version=__version__,
    description='Django tree based on foreign key',
    long_description=long_description,
    zip_safe=False,
    author='Razzhivin Alexander',
    author_email='admin@httpbots.com',
    url='https://github.com/RANUX/django-fktree',
    download_url='https://github.com/RANUX/django-fktree/downloads',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django',
        ### Required to build documentation
        # 'sphinx',
    ],
    test_suite='tests',
    tests_require=['nose','django', 'django-nose', 'coverage'],
    classifiers = ['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)