#!/usr/bin/env python
import os
import sys

import socket

if __name__ == "__main__":
    root = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(root, 'site-packages-pip-fail'))
    sys.path.insert(0, os.path.join(root, 'site-packages-upgrade-stop'))
    sys.path.insert(0, os.path.join(root, 'site-packages-update'))
    sys.path.insert(0, os.path.join(root, '..','env','Lib','site-packages'))
    if not 'SERVER_SOFTWARE' in os.environ:         
        sys.path.insert(0, os.path.join(root, 'site-packages-pyd', socket.gethostname()))	
        print socket.gethostname()
		
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csblog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
