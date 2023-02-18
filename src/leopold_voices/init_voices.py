from gtts import gTTS


def init_tts():
    tts = gTTS(text="Привет я твой голосовой помощник Леопольд", lang='ru')
    tts.save("leo_start.mp3")

    tts = gTTS(text="Имя может быть любым каким только ты пожелаешь давай смелее друг мой", lang='ru')
    tts.save("leo_1.mp3")

    tts = gTTS(text="Регион где будет проходить ваш хакатон не слишиком холодно и не особо жарко ну чтото среднее")
    tts.save("leo_2.mp3")

    print("Леопольд готов к работе")
