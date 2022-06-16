from rest_framework import serializers
from .models import Audio, Video_Extract

class AudioSerializer(serializers.ModelSerializer):
   """
   Audio Serializer
   """
   class Meta:
        model = Audio
        fields = '__all__'

class VideoExtractSerializer(serializers.ModelSerializer):
   """
   Audio Serializer
   """
   class Meta:
        model = Video_Extract
        fields = '__all__'

