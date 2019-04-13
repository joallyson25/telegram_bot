import telepot
from chatbot import Chatbot

telegram = telepot.Bot("KEY FROM TELEGRAM")
bot = Chatbot("RedX")  # Cria um novo bot e dá nome a ele

# Função para puxar as novas mensagens
# (esta é a que recebe vários informações em forma de dict)
#print(telegram.getUpdates())

# Função para enviar novas mensagens
# (recebe vários informações em forma de dict)
#print(telegram.sendMessage(coloque o núm do chat id, 'digite a msg'))

# É chamada sempre que há nova msg
def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    # O método 'glance' é para facilitar pegar a msg de uma forma
    # mais fácil do que a da linha acima; Ele vai filtrar 'msg'
    # e entregar 3 valores, que abaixo foram atribuidos a 3 variáveis
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    # Envia 'resp' processado pelo bot no telegram
    telegram.sendMessage(chatID, resp)


# Procura sempre se há novas mensagens, quando tiver,
# ele chamará a função 'recebendoMsg' para tratar
telegram.message_loop(recebendoMsg)

print('Módulo Telegram ativo!')

# Para não deixar a aplicação parar
while True:
    pass
