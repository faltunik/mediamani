import uuid
from django.db import models
from django.db.models.signals import post_save

from .utils import speed_audio, extract_audio

# Create your models here.

class Audio(models.Model):
    audio = models.FileField(upload_to='audio/')
    speed = models.FloatField()
    audio_speed = models.FileField(upload_to='audio_x/', blank=True, null= True)
    
    def __str__(self):
        return self.audio.name

def speedup_audio(sender,instance,created,**kwargs):
    output = speed_audio.delay(audio_id=instance.id, input=instance.audio.path, speed=instance.speed)


post_save.connect(speedup_audio,sender=Audio,dispatch_uid=uuid.uuid4)

class Video_Extract(models.Model):
    video = models.FileField(upload_to='video/')
    audio_extract = models.FileField(upload_to='audio_extract/', blank=True, null= True)
    
    def __str__(self):
        return self.video.name

def audio_extract(sender,instance,created,**kwargs):
    extract_audio.delay(video_id=instance.id, input=instance.video.path)


post_save.connect(audio_extract,sender=Video_Extract,dispatch_uid=uuid.uuid4)
