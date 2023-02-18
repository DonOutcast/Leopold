# import pyttsx3

# tts = pyttsx3.init()

# Задать голос по умолчанию
# ru_voice_id = "com.apple.speech.synthesis.voice.milena.premium"
# tts.setProperty('voice', ru_voice_id)

# Попробовать установить предпочтительный голос
# voices = tts.getProperty("voices")
# for voice in voices:
#     if voice.name == 'Yuri':
#         tts.setProperty('voice', voice.id)
# tts.setProperty("rate", 158)
# tts.save_to_file("Привет, я твой голосовой помощник Леопольд", "leopold_voices/first_help.mp3")
# # tts.runAndWait()


from gtts import gTTS

tts = gTTS(text="Привет я твой голосовой помощник Леопольд", lang='ru')
tts.save("leopold_voices/leo_start.mp3")

tts = gTTS(text="Имя может быть любым каким только ты пожелаешь давай смелее друг мой", lang='ru')
tts.save("leopold_voices/leo_1.mp3")

tts = gTTS(text="Можешь нажать на кнопку и узнать где ты живёшь", lang='ru')
tts.save("leopold_voices/leo_2.mp3")

tts = gTTS(text="Можешь загружить картинку, которая тебе нравится", lang='ru')
tts.save("leopold_voices/leo_3.mp3")

tts = gTTS(text="Расскажи кратко о своём проекте, выложи основную идею", lang='ru')
tts.save("leopold_voices/leo_4.mp3")

tts = gTTS(text="Опиши проекты, в которых ты участвовал", lang='ru')
tts.save("leopold_voices/leo_5.mp3")

tts = gTTS(text="Укажи адрес регистрации по паспорту, не ошибёшься", lang='ru')
tts.save("leopold_voices/leo_6.mp3")

tts = gTTS(text="В браузере надо открыть страницу с твоим резюме, скопировать адрес командной строки и ввести сюда", lang='ru')
tts.save("leopold_voices/leo_7.mp3")

tts = gTTS(text="Сделай тоже самое что и в предыдущем, только открой страницу со своим видео", lang='ru')
tts.save("leopold_voices/leo_8.mp3")

tts = gTTS(text="Поздравляю, вы большой молодец!", lang='ru')
tts.save("leopold_voices/leo_9.mp3")