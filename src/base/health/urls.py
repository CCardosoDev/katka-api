from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'base'
urlpatterns = [
    url(r'^$', views.HealthView.as_view(), name='index'),
]
