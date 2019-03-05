# Módulo recolhecedor de voz
import speech_recognition as sr

rec = sr.Recognizer()

# Chama o módulo microfone para gravação da fala
with sr.Microphone() as fala:
    # Método listen vai ouvir o que iremos falar
    frase = rec.listen(fala)

# Transformar o que foi dito no microfone e
# retorna um texto com o reconhecedor de voz sphinx
#print(rec.recognize_sphinx(frase))

# Transformar o que foi dito no microfone e
# retorna uma texto com o reconhecedor de voz do Google
# que também pode reconhecer em português
print(rec.recognize_google(frase, language='pt'))
