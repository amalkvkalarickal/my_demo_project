# main.py
import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
application = get_wsgi_application()
