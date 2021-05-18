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

    chat_id = '-330418276'
    print(chat_id)
    usuariosStartados.append(chat_id)
    link_noticia = ''
    link_noticia2 = ''
    link_noticia3 = ''
    link_noticia4 = ''
    link_noticia5 = ''
    link_noticia6 = ''
    link_noticia7 = ''
    link_noticia8 = ''
    link_noticia9 = ''
    link_noticia10 = ''
    link_noticia11 = ''
    link_noticia12 = ''
    link_noticia13 = ''
    link_noticia14 = ''
    link_noticia15 = ''
    link_noticia16 = ''
    link_noticia17 = ''

    while True:
        time.sleep(30)
        page = requests.get("https://livecoins.com.br/category/altcoins/")
        soup = BeautifulSoup(page.content, 'html.parser')

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='entry-title td-module-title')
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

#################### SEGUNDA NOTICIA ##########################

        #time.sleep(10)
        page = requests.get("https://livecoins.com.br/category/bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='entry-title td-module-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link2 = noticia_name.get('href')
            # print(names)
            print(link2)

        if link_noticia2 != link2:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link2)
            link_noticia2 = link2

#################### TERCEIRA NOTICIA ##########################
        page = requests.get("https://livecoins.com.br/category/blockchain/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='entry-title td-module-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link3 = noticia_name.get('href')
            # print(names)
            print(link3)

        if link_noticia3 != link3:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link3)
            link_noticia3 = link3

#################### QUARTA NOTICIA ##########################

        page = requests.get("https://portaldobitcoin.com/mineracao/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link4 = noticia_name.get('href')
            # print(names)
            print(link4)

        if link_noticia4 != link4:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link4)
            link_noticia4 = link4

#################### QUINTA NOTICIA ##########################
        page = requests.get("https://portaldobitcoin.com/blockchain/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link5 = noticia_name.get('href')
            # print(names)
            print(link5)

        if link_noticia5 != link5:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link5)
            link_noticia5 = link5


#################### SEXTA NOTICIA ##########################

        page = requests.get("https://portaldobitcoin.com/criptomoedas/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link6 = noticia_name.get('href')
            # print(names)
            print(link6)

        if link_noticia6 != link6:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link6)
            link_noticia6 = link6

#################### SETIMA NOTICIA ##########################

        page = requests.get("https://guiadobitcoin.com.br/categoria/bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link7 = noticia_name.get('href')
            # print(names)
            print(link7)

        if link_noticia7 != link7:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link7)
            link_noticia7 = link7

#################### OITAVA NOTICIA ##########################
        page = requests.get("https://guiadobitcoin.com.br/categoria/exchanges/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link8 = noticia_name.get('href')
            # print(names)
            print(link8)

        if link_noticia8 != link8:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link8)
            link_noticia8 = link8

#################### NONA NOTICIA ##########################
        page = requests.get("https://guiadobitcoin.com.br/categoria/altcoins/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]

            link9 = noticia_name.get('href')
            # print(names)
            print(link9)

        if link_noticia9 != link9:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link9)
            link_noticia9 = link9

#################### DECIMA NOTICIA ##########################
        page = requests.get("https://guiadobitcoin.com.br/categoria/blockchain/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link10 = noticia_name.get('href')
            # print(names)
            print(link10)

        if link_noticia10 != link10:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link10)
            link_noticia10 = link10

#################### DECIMA PRIMEIRA NOTICIA ##########################
        page = requests.get("https://www.newsbtc.com/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='five columns bitcoin')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link11 = noticia_name.get('href')
            # print(names)
            print(link11)

        if link_noticia11 != link11:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link11)
            link_noticia11 = link11


#################### DECIMA SEGUNDA NOTICIA ##########################
        page = requests.get("https://cryptonews.com")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='cn-tile row article')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link12 = noticia_name.get('href')
            link12 = 'https://cryptonews.com' + link12
            # print(names)
            print(link12)

        if link_noticia12 != link12:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link12)
            link_noticia12 = link12

#################### DECIMA TERCEIRA NOTICIA ##########################
        page = requests.get("https://bitcoinmagazine.com/articles")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='bm-card category-list--card')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]

            link13 = noticia_name.get('href')
            link13 = 'https://bitcoinmagazine.com' + link13
            # print(names)
            print(link13)

        if link_noticia13 != link13:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link13)
            link_noticia13 = link13

#################### DECIMA QUARTA NOTICIA ##########################
        page = requests.get("https://news.bitcoin.com/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-big-grid-meta')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link14 = noticia_name.get('href')
            # print(names)
            print(link14)

        if link_noticia14 != link14:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link14)
            link_noticia14 = link14

#################### DECIMA QUINTA NOTICIA ##########################


#################### DECIMA SEXTA NOTICIA ##########################
        page = requests.get("https://www.bitcoinnews.com.br/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='owl-mod-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link16 = noticia_name.get('href')
            # print(names)
            print(link16)

        if link_noticia16 != link16:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link16)
            link_noticia16 = link16

#################### DECIMA SETIMA NOTICIA ##########################

        page = requests.get("https://br.cointelegraph.com")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-preview-item-card__header')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link17 = noticia_name.get('href')
            # print(names)
            print(link17)

        if link_noticia17 != link17:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link17)
            link_noticia17 = link17


def pegaUltimaMensagem(msg):
    if msg['text'] == 'envia':
        envia_msg()




#telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(10)
    envia_msg()
