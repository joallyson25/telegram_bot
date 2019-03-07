import json
import sys  # Descobrir a plataforma
import os  # Para exec aplicação do Windows
import subprocess as s  # Para exec aplicação do Linux


class Chatbot():

    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["Will", "Joallyson"], {"oi": "Olá, qual o seu nome?", "tchau": "tchau"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None, ]

    """ 
    Recebe a frase digitada pelo usuário, 
    torna toda ela minúscula e retorna 
    """
    def escuta(self, frase=None):
        if frase is None:
            frase = input(">: ")
        frase = str(frase)
        if 'execut' in frase:
            return frase
        frase = frase.lower()
        frase = frase.replace("é", "eh")
        return frase

    """ 
    Verifica se a frase é conhecida,
    se for nova e tiver a palavra chave 'aprende'
    ele irá aprender, agora se a última frase
    do histórico for 'Olá, qual o seu nome?' o bot
    chama a func pegaNome() e respondeNome(),
    no final retorna uma nova frase;
    Caso seja um comando a func eval() vai ser
    utilizada para processar e retornar um valor;
    Caso não seja uma frase reconhecida, não seja
    comando e não tenha a palavra chave 'aprende'
    ele retorna a frase 'não entendi'   
    """
    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]
        if 'aprend' in frase:
            return 'Digite a frase: '
        # Responde frases que dependem do histórico
        ultimaFrase = self.historico[-1]  # Pra não ficar fazendo vários acessos a variável
        if ultimaFrase == "Olá, qual o seu nome?":
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Digite a frase: ':
            self.chave = frase
            return 'Digite a resposta: '
        if ultimaFrase == 'Digite a resposta: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Beleza, aprendido! \u263a'  # Salvar msg na mem (arquivo .json)
        try:
            resp = eval(frase)
            return str(resp)
        except:
            pass
        return "Não entendi"

    """
    Se a frase tiver o trecho 'o meu nome eh'
    esse trecho será removido e assim a func 
    retorna apenas o nome
    """
    def pegaNome(self, frase):
        if "o meu nome eh " in frase:
            nome = frase[14:].title()
        else:
            nome = frase
        return nome

    """
    Se for um nome conhecido ele retorna a frase
    com o prefixo 'Eaew', caso n seja, 'Muito prazer'
    e salva o nome desta pessoa no arquivo .json
    """
    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = "Eaew "
        else:
            frase = "Muito prazer "
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome

    """
    Salvar nomes e frases no arquivo .json
    """
    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    """
    Se na resposta do bot, a frase tiver a palavra 'executa',
    ele irá verif em qual SO este programa está rodando, se windows ou
    linux, e irá executar o comando desejado pelo usuário
    através da biblioteca 'os' do Windows ou 'subprocess' do linux
    e no final add a frase na var histórico
    """
    def fala(self, frase):
        if 'executar' in frase:
            plataforma = sys.platform
            comando = frase.replace('executar ', '')  # Elimina 'executa' e copia o resto da frase
            if 'win' in plataforma:
                os.startfile(f'{comando}')
            if 'linux' in plataforma:
                try:
                    s.Popen(comando.lower())  # Executar aplicação do linux
                except FileNotFoundError:
                    s.Popen(['xdg-open', comando])  # Abrir sites
        else:
            print(frase)
        self.historico.append(frase)


