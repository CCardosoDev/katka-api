from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=False)
