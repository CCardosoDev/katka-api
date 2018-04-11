from __future__ import unicode_literals

from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=False)
