import uuid
from django.db import models
from django.db.models.signals import post_save

from .utils import speed_audio

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
