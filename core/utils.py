import subprocess

def speed_audio(audio_name, input, speed=3):
    """
    Speed up the audio
    """
    output = f"./audiox/{audio_name}_speed.mp3"
    s = f"ffmpeg -i {input} -filter:a atempo={speed} {output}"
    cmd = s.split(" ")
    subprocess.check_output(cmd)
    return output