from rest_framework import serializers
from django.conf import settings
from .models import Route
from django.conf import settings

class StopNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields=['stop_id']