import os
from gtts import gTTS
import time


def generate_audio(prompt, audio_directory):
    tts = gTTS(text=prompt, lang='en', slow=False)
    audio_file_path = os.path.join(audio_directory, "output.mp3")
    time.sleep(10)
    tts.save(audio_file_path)