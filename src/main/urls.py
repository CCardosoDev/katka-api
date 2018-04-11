from __future__ import unicode_literals

from django.conf.urls import include, url

patterns = [
    url(r'^error/', include('base.error.urls', namespace='error')),
    url(r'^health/', include('base.health.urls', namespace='health')),
]

urlpatterns = [
    url(r'^katka-api/', include(patterns)),
]
