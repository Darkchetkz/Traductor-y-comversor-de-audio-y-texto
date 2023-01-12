import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Escuchando...!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        print("lo que dijiste: {} " .format(text))

    except:
        print("Sorry could not recognize your voice")