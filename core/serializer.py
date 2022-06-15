from rest_framework import serializers
from .models import Audio

class AudioSerializer(serializers.ModelSerializer):
   """
   Audio Serializer
   """
   class Meta:
        model = Audio
        fields = '__all__'
