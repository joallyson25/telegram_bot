from chatbot import Chatbot
import pyttsx3  # reprodução em voz do texto
import speech_recognition as sr  # Reconhecimento de voz

# Inicializa a engine e define o idioma da voz
en = pyttsx3.init()
en.setProperty('voice', 'brazil')
rec = sr.Recognizer()


# Herença da classe Chatbot e polimorfismo
class BotFalante(Chatbot):

    def escuta(self, frase=None):
        try:
            with sr.Microphone() as mic:
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala, language='pt')
            print(frase)  # Qual texto ele está identificando
        except sr.UnknownValueError:
            print('Erro ao identificar a voz')
            return ''
        # Chamando a função antiga do Chatbot
        return super().escuta(frase=frase)

    def fala(self, frase):
        en.say(frase)
        en.runAndWait()
        super().fala(frase)


Bot = BotFalante('Felipe')

while True:

    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)

    if resp == "tchau":
        break

