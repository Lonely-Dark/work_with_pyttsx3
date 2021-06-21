import pyttsx3

RU_LANG = ""

tts = pyttsx3.init()

voices = [i.id for i in tts.getProperty("voices")]
print(voices)

tts.setProperty("voice", RU_LANG)
tts.say("Проверка")
tts.runAndWait()