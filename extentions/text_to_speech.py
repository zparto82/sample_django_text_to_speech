from django.conf import settings
from gtts import gTTS


BASE_DIR = settings.BASE_DIR / "media/audios"
language = 'en'


def text_to_speech(text:str):
    text = text.strip()
    name = text.replace(" ", "")

    file_name = f"{name}.mp3"
    audio_file = BASE_DIR / file_name
    
    sound = gTTS(text=text, lang=language, slow=False)
    sound.save(audio_file)
    
    return file_name
  
