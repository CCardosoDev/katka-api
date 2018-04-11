import os

from django.core.wsgi import get_wsgi_application

from raven.middleware import Sentry

# Directly assign to os.environ instead of using os.environ.setdefault as the former plays nice
# with having multiple django sites run from one WSGIProcessGroup, as done on test server.
# There seems to be no use case where the DJANGO_SETTINGS_MODULE needs to be defined elsewhere.
# See comment in default Django project wsgi
os.environ["DJANGO_SETTINGS_MODULE"] = "main.settings"


application = Sentry(get_wsgi_application())
