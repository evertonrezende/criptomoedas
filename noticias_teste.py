import requests
import telepot
import json
import time
from bs4 import BeautifulSoup
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


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
    link_noticia36 = ''

    try:
        html = urlopen("https://guiadobitcoin.com.br/categoria/noticias/")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        res = BeautifulSoup(html.read(), "html5lib")
        tags = res.find("div", {"class": "col-md-9"})
        for tag in tags:
            link36 = tag.get('href')
            print(link36)

    #mandarMensagem(chat_id, link36)
        #link_noticia36 = link36



def pegaUltimaMensagem(msg):
    if msg['text'] == 'envia':
        envia_msg()



#telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(2)
    envia_msg()
    #t = Timer(10)
    #t.start()