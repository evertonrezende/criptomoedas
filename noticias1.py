import requests
import telepot
import json
import time
from bs4 import BeautifulSoup
import threading


class Timer(threading.Thread):

    def __init__(self, segundos):
        self.runTime = segundos
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.runTime)
        print("Executado!")
        envia_msg()


usuariosStartados = []

telegramBot = telepot.Bot('468489595:AAHak-3V4uol8oxHyVRpYCj60Usi7Eo0sto')


def mandarMensagem(chat_id, texto):
    # def mandarMensagem(idUsuario, texto):
    telegramBot.sendMessage(chat_id, texto, parse_mode="HTML")
    # telegramBot.sendMessage(idUsuario, texto, parse_mode="HTML")


def envia_msg():
    #telegramUpdates = telegramBot.getUpdates()
    #print(telegramUpdates)
    # idUsuario = telegramUpdates[-1]['message']['chat']['id']
    #chat_id = telegramUpdates[-1]['message']['chat']['378241672']
    chat_id = '-330418276'
    print(chat_id)
    usuariosStartados.append(chat_id)
    link_noticia = ''

    while True:
        time.sleep(10)
        page = requests.get("https://br.cointelegraph.com")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-preview-item-card__header')
        cont = 0
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]
            link = noticia_name.get('href')
            #print(names)
            print(link)

        if link_noticia != link:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link)
            link_noticia = link


def pegaUltimaMensagem(msg):
    if msg['text'] == 'envia':
        envia_msg()



#telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(10)
    envia_msg()
    #t = Timer(10)
    #t.start()