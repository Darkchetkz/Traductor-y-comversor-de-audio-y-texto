
from googletrans import Translator

# Crear un objeto de traducción
translator = Translator()

# introducir un texto en inglés 

#crea un siclo 

while True:
    text = input("Ingresa texto: ")
    translation = translator.translate(text, src='es', dest='en')
    print(translation.text)

