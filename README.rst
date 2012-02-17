About
===============================================
django-fktree - pre-order traversal tree in django based on foreign keys

Dependencies
===============================================
pip-requirements.txt

Installation
===============================================
Installation from github::

    pip install -e git+https://github.com/RANUX/django-fktree#egg=django-fktree


Examples
===============================================
Catalog with tree structure::

    from fktree.models import Node

    class Catalog(Node):
        ...

For more information see fktree.tests
