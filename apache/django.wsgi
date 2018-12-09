
import os
import sys
import socket

# root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# workspace = os.path.dirname(root)

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(os.path.abspath(__file__)) 
project = os.path.dirname(apache_configuration) # djangocms35-csblog
workspace = os.path.dirname(project) # djangocms

sys.path.insert(0, os.path.join(project, 'site-packages-update'))
sys.path.insert(0, os.path.join(workspace, 'env', 'lib', 'site-packages'))
# if not 'SERVER_SOFTWARE' in os.environ:         
# 	sys.path.insert(0, os.path.join(project, 'site-packages-pyd', socket.gethostname()))	

sys.stdout = sys.stderr

sys.path.append(project)
#sys.path.append(workspace)

print sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = "csblog.settings"

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import django
print django.VERSION
