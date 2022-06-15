from rest_framework import serializers

class AudioSerializer(serializers.Serializer):
   """
   Audio Serializer
   """
   audio = serializers.FileField()
   speed = serializers.FloatField()