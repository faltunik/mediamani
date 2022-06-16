from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializer import AudioSerializer, VideoExtractSerializer




# Create your views here.

@api_view(['POST'])
def audio_speed(request):
    serializer = AudioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def audio_extracter(request):
    serializer =VideoExtractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)







