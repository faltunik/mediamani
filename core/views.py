from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AudioSerializer

# Create your views here.

@api_view(['POST'])
def audio_speed(request):
    serializer = AudioSerializer(data=request.data)
    print(request.data)
    print(request.data['audio'].name)
    print(type(request.data['audio']))
    print(request.data['speed'])
    if serializer.is_valid():
        # serializer.save()
        print("audio is getting processed")
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
