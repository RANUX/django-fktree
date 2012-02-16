# -*- coding: UTF-8 -*-
from django.conf import settings


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


PATH_SEPARATOR = getattr(settings, 'TREE_PATH_SEPARATOR', '/')
PATH_DIGITS = getattr(settings, 'TREE_PATH_DIGITS', 10)