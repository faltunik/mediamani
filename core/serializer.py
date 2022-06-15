from rest_framework import serializers
from .models import Audio

class AudioSerializer(serializers.Serializer):
   """
   Audio Serializer
   """
   class Meta:
        model = Audio
        fields = '__all__'
