from django.contrib import admin
from django.urls import include, path

patterns = [
    path('health/', include('main.health.urls', namespace='health')),
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('api/', include(patterns)),
]
