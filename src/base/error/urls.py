from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'base.error'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^silent/$', views.SilentExceptionView.as_view(), name='silent'),
    url(r'^any/$', views.BroadExceptionView.as_view(), name='any')
]
