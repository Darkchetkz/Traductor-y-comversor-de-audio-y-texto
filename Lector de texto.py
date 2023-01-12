import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
text = "Hola como estas Kihiok"
engine.say(text)

another_text = "wen toto kihiok"
engine.say(another_text)
engine.runAndWait()