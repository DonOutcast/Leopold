import pyttsx3

tts = pyttsx3.init()

# Задать голос по умолчанию
ru_voice_id = "com.apple.speech.synthesis.voice.milena.premium"
tts.setProperty('voice', ru_voice_id)

# Попробовать установить предпочтительный голос
voices = tts.getProperty("voices")
for voice in voices:
    if voice.name == 'Yuri':
        tts.setProperty('voice', voice.id)
tts.setProperty("rate", 158)
tts.save_to_file("Привет, я твой голосовой помощник Леопольд", "test.mp3")
tts.runAndWait()