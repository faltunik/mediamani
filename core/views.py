from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializer import AudioSerializer
from .utils import speed_audio
from .models import Audio




# Create your views here.

@api_view(['POST'])
def audio_speed(request):
    serializer = AudioSerializer(data=request.data)
    if serializer.is_valid():
        audio_ins = serializer.save()
        audio = Audio.objects.get(id=audio_ins.id)
        print("audio is getting processed")
        print(audio.audio.name)
        print(audio.audio.path)
        speedex = speed_audio(audio.audio.name.replace("/", ""), audio.audio, request.data['speed'] )
        print("audio processed")
        serializer.save(audio_speed = speedex)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)





