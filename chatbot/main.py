from chatbot import *

Bot = Chatbot("Carlos")

while True:

    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)

    if resp == "tchau":
        break

