from django.utils.timezone import now

from main.health import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    """
    RestFramework view responsible for delivering an overview of this
    project's health
    """
    serializer_class = serializers.HealthSerializer
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class({"date": now()}).data)
