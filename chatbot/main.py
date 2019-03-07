from chatbot import Chatbot
import pyttsx3  # reprodução em voz do texto
import speech_recognition as sr  # Reconhecimento de voz

# Inicializa a engine e define o idioma da voz
en = pyttsx3.init()
en.setProperty('voice', 'brazil+f1')  # +f -> voz feminina e m masc
rec = sr.Recognizer()


# Herença da classe Chatbot e polimorfismo
class BotFalante(Chatbot):

    # Cria função de mesmo nome da classe pai
    # mas sobrescreve (polimorfismo)
    def escuta(self, frase=None):
        try:
            with sr.Microphone() as mic:
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala, language='pt')
            print(frase)  # Qual texto ele está identificando
        except sr.UnknownValueError:
            print('Erro ao identificar a voz')
            return ''
        # Chama a função escuta() do arquivo Chatbot
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

