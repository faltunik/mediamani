import subprocess

from celery import shared_task 

from .manager import task_lock
from .models import Audio

@shared_task(bind=True)
def speed_audio(self,audio_id, input, speed=3):
    """
    Speed up the audio
    """
    taskid = self.request.id
    with task_lock("task-lock", taskid , lock_expire_seconds=10) as acquired:
        if acquired:
            audio_ins = Audio.objects.get(id = audio_id)
            output = f"./audiox/{audio_ins.name}_speed.mp3"
            s = f"ffmpeg -i {input} -filter:a atempo={speed} {output}"
            cmd = s.split(" ")
            subprocess.check_output(cmd)
            audio_ins.audio_speed = output
            audio_ins.save(update_fields = ['audio_speed'])