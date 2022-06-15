from django.db import models

# Create your models here.

class Audio(models.Model):
    audio = models.FileField(upload_to='audio/')
    speed = models.FloatField()
    audio_speed = models.FileField(upload_to='audio_x/', blank=True, null= True)
    
    def __str__(self):
        return self.audio.name
