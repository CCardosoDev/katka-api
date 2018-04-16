from django.urls import include, path

patterns = [
    path('error/', include('base.error.urls', namespace='error')),
    path('health/', include('base.health.urls', namespace='health')),
]

urlpatterns = [
    path('katka-api/', include(patterns)),
]
