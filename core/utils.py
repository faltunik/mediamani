import subprocess

from celery import shared_task 

from .manager import task_lock
import core.models as m

@shared_task(bind=True)
def speed_audio(self,audio_id, input, speed=3):
    """
    Speed up the audio
    """
    taskid = self.request.id
    with task_lock("task-lock", taskid , lock_expire_seconds=10) as acquired:
        if acquired:
            audio_ins = m.Audio.objects.get(id = audio_id)
            print("------------------------------------------------------------------")
            print("file name or path is: ", audio_ins.audio.name)
            rename = str(audio_ins.audio.name).replace("/", "_")
            print("------------------------------------------------------------------")
            output = f"./audiox/{rename}_speed.mp3"
            s = f"ffmpeg -i {input} -filter:a atempo={speed} {output}"
            cmd = s.split(" ")
            subprocess.check_output(cmd)
            audio_ins.audio_speed = output
            audio_ins.save(update_fields = ['audio_speed'])


# cmd = ['ffmpeg', '-i', 'inputvid.mp4', f'demoaudio{a}.mp3']

@shared_task(bind=True)
def extract_audio(self,video_id, input):
    taskid = self.request.id
    with task_lock("task-lock", taskid , lock_expire_seconds=10) as acquired:
        if acquired:
            video_ins = m.Video_Extract.objects.get(id = video_id)
            print("------------------------------------------------------------------")
            print("file name or path is: ", video_ins.video.name)
            rename = str(video_ins.video.name).replace("/", "_")
            print("------------------------------------------------------------------")
            output = f"./audio_extract/{rename}_extract.mp3"
            s = f"ffmpeg -i {input} {output}"
            cmd = s.split(" ")
            subprocess.check_output(cmd)
            video_ins.audio_extract = output
            video_ins.save(update_fields = ['audio_extract'])

