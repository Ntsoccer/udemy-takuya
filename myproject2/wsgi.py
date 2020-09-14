import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTING_MODULE","myproject2.settings")

application=Cling(get_wsgi_application())

