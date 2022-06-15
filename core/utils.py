import subprocess

from celery import shared_task 

from .manager import task_lock

@shared_task(bind=True)
def speed_audio(self,audio_name, input, speed=3):
    """
    Speed up the audio
    """

    task_id = self.request.id
    try:
        output = f"./audiox/{audio_name}_speed.mp3"
        s = f"ffmpeg -i {input} -filter:a atempo={speed} {output}"
        cmd = s.split(" ")
        subprocess.check_output(cmd)
        return output
    except Exception as e:
        if self.AsyncResult(self.request.id).state == "FAILURE":
            print("task failed")
            self.revoke(self.request.id, terminate=True)
        print(e)
        return None