import os

import django
from django.core.handlers.wsgi import WSGIHandler

os.environ["DJANGO_SETTINGS_MODULE"] = "main.settings"


def get_wsgi_application():
    django.setup()
    return WSGIHandler()


application = get_wsgi_application()
