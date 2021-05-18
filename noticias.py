import requests
import telepot
import json
import time
from bs4 import BeautifulSoup
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

class Timer(threading.Thread):

    def __init__(self, segundos):
        self.runTime = segundos
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.runTime)
        print("Executado!")
        envia_msg()


usuariosStartados = []

telegramBot = telepot.Bot('655554061:AAHvjdHx67xOO3sBqW4Yz8btqTw5KC7xY_U')


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
    link_noticia18 = ''
    link_noticia19 = ''
    link_noticia20 = ''
    link_noticia21 = ''
    link_noticia22 = ''
    link_noticia23 = ''
    link_noticia24 = ''
    link_noticia25 = ''
    link_noticia26 = ''
    link_noticia27 = ''
    link_noticia28 = ''
    link_noticia29 = ''
    link_noticia30 = ''
    link_noticia31 = ''
    link_noticia32 = ''
    link_noticia33 = ''
    link_noticia34 = ''
    link_noticia35 = ''
    link_noticia36 = ''

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

        #page = requests.get("https://portaldobitcoin.com/mineracao/")
        #soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        #noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        #noticia_name_list_items = noticia_name_list.find_all('a')
        #for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            #link4 = noticia_name.get('href')
            # print(names)
            #print(link4)

        #if link_noticia4 != link4:
            # lista_noticia.append(link)
            #mandarMensagem(chat_id, link4)
            #link_noticia4 = link4

#################### QUINTA NOTICIA ##########################
        #page = requests.get("https://portaldobitcoin.com/blockchain/")
        #soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        #noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        #noticia_name_list_items = noticia_name_list.find_all('a')
        #for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            #link5 = noticia_name.get('href')
            # print(names)
            #print(link5)

        #if link_noticia5 != link5:
            # lista_noticia.append(link)
            #mandarMensagem(chat_id, link5)
            #link_noticia5 = link5


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

#        page = requests.get("https://guiadobitcoin.com.br/categoria/bitcoin/")
 #       soup = BeautifulSoup(page.content, 'html.parser')
#
 #       # Pegar todo o texto da div BodyText
  #      noticia_name_list = soup.find(class_='post-title')
   #     # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
#        noticia_name_list_items = noticia_name_list.find_all('a')
#        for noticia_name in noticia_name_list_items:
#            # names = noticia_name.contents[0]
#            link7 = noticia_name.get('href')
#            # print(names)
#            print(link7)

#        if link_noticia7 != link7:
#            # lista_noticia.append(link)
#            mandarMensagem(chat_id, link7)
#            link_noticia7 = link7

#################### OITAVA NOTICIA ##########################
#        page = requests.get("https://guiadobitcoin.com.br/categoria/exchanges/")
#        soup = BeautifulSoup(page.content, 'html.parser')


        # Pegar todo o texto da div BodyText
#        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
#        noticia_name_list_items = noticia_name_list.find_all('a')
 #       for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
#            link8 = noticia_name.get('href')
#            # print(names)
#            print(link8)

#        if link_noticia8 != link8:
#            # lista_noticia.append(link)
#            mandarMensagem(chat_id, link8)
#            link_noticia8 = link8

#################### NONA NOTICIA ##########################
#        page = requests.get("https://guiadobitcoin.com.br/categoria/altcoins/")
#        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
#        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
 #       noticia_name_list_items = noticia_name_list.find_all('a')
#      for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]

#            link9 = noticia_name.get('href')
            # print(names)
#            print(link9)

 #       if link_noticia9 != link9:
 #           # lista_noticia.append(link)
 #           mandarMensagem(chat_id, link9)
 #           link_noticia9 = link9

#################### DECIMA NOTICIA ##########################
#        page = requests.get("https://guiadobitcoin.com.br/categoria/blockchain/")
#        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
#        noticia_name_list = soup.find(class_='post-title')
#        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
#        noticia_name_list_items = noticia_name_list.find_all('a')
#        for noticia_name in noticia_name_list_items:
#            # names = noticia_name.contents[0]
#            link10 = noticia_name.get('href')
            # print(names)
#            print(link10)

#        if link_noticia10 != link10:
            # lista_noticia.append(link)
#            mandarMensagem(chat_id, link10)
#            link_noticia10 = link10

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


#################### DECIMA OITAVA NOTICIA ##########################

        page = requests.get("https://infochain.com.br/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='entry-header-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link18 = noticia_name.get('href')
            # print(names)
            print(link18)

        if link_noticia18 != link18:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link18)
            link_noticia18 = link18


#################### DECIMA NONA NOTICIA ##########################

        page = requests.get("https://webitcoin.com.br/category/bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='col-xs-12 col-xl-4 col-md-3')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link19 = noticia_name.get('href')
            # print(names)
            print(link19)

        if link_noticia19 != link19:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link19)
            link_noticia19 = link19


#################### VIGESIMA NOTICIA ##########################

        page = requests.get("https://webitcoin.com.br/category/altcoins/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='col-xs-12 col-xl-4 col-md-3')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link20 = noticia_name.get('href')
            # print(names)
            print(link20)

        if link_noticia20 != link20:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link20)
            link_noticia20 = link20

#################### VIGESIMA PRIMEIRA NOTICIA ##########################

        page = requests.get("https://webitcoin.com.br/category/tecnologia/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='col-xs-12 col-xl-4 col-md-3')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link21 = noticia_name.get('href')
            # print(names)
            print(link21)

        if link_noticia21 != link21:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link21)
            link_noticia21 = link21


#################### VIGESIMA SEGUNDA NOTICIA ##########################
        page = requests.get("https://cointimes.com.br/categoria/noticias/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='card-picture__title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link22 = noticia_name.get('href')
            # print(names)
            print(link22)

        if link_noticia22 != link22:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link22)
            link_noticia22 = link22


#################### VIGESIMA TERCEIRA NOTICIA ##########################

        #page = requests.get("https://cointimes.com.br/categoria/altcoins/")
        #soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        #noticia_name_list = soup.find(class_='card-picture__title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        #noticia_name_list_items = noticia_name_list.find_all('a')
        #for noticia_name in noticia_name_list_items:
            #link23 = noticia_name.get('href')

            #print(link23)

        #if link_noticia23 != link23 and link_noticia23 != link_noticia22:
            # lista_noticia.append(link)
            #mandarMensagem(chat_id, link23)
            #link_noticia23 = link23


#################### VIGESIMA QUARTA NOTICIA ##########################

        page = requests.get("https://cointimes.com.br/categoria/blockchain/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='card-picture__title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link24 = noticia_name.get('href')
            # print(names)
            print(link24)

        if link_noticia24 != link24 and link_noticia24 != link_noticia22:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link24)
            link_noticia24 = link24

#################### VIGESIMA QUINTA NOTICIA ##########################

        #page = requests.get("https://cointimes.com.br/categoria/bitcoin/")
        #soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        #noticia_name_list = soup.find(class_='card-picture__title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        #noticia_name_list_items = noticia_name_list.find_all('a')
        #for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            #link25 = noticia_name.get('href')
            # print(names)
            #print(link25)

        #if link_noticia25 != link25 and link_noticia25 != link_noticia22:
            # lista_noticia.append(link)
            #mandarMensagem(chat_id, link25)
            #link_noticia25 = link25

#################### VIGESIMA SEXTA NOTICIA ##########################

        page = requests.get("https://criptozoom.com/noticias/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link26 = noticia_name.get('href')
            # print(names)
            print(link26)

        if link_noticia26 != link26 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link26)
            link_noticia26 = link26

#################### VIGESIMA SETIMA NOTICIA ##########################

        page = requests.get("https://criptozoom.com/noticias-bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link27 = noticia_name.get('href')
            # print(names)
            print(link27)

        if link_noticia27 != link27 and link_noticia27 != link_noticia26:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link27)
            link_noticia27 = link27

#################### VIGESIMA OITAVA NOTICIA ##########################

        page = requests.get("https://www.btcsoul.com/category/noticias/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link28 = noticia_name.get('href')
            # print(names)
            print(link28)

        if link_noticia28 != link28 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link28)
            link_noticia28 = link28

#################### VIGESIMA NONA NOTICIA ##########################

        page = requests.get("https://jornaldobitcoin.info/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='item item-1 clearfix')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link29 = noticia_name.get('href')
            link29 = 'https://jornaldobitcoin.info' + link29
            print(link29)

        if link_noticia29 != link29 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link29)
            link_noticia29 = link29


#################### TRIGESIMA NOTICIA ##########################

        page = requests.get("https://bitcoinist.com/category/bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='news-content cf')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link30 = noticia_name.get('href')
            # print(names)
            print(link30)

        if link_noticia30 != link30 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link30)
            link_noticia30 = link30


#################### TRIGESIMA PRIMEIRA NOTICIA ##########################

        page = requests.get("https://www.brbitcoin.com.br/category/noticias/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='title-post')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link31 = noticia_name.get('href')
            # print(names)
            print(link31)

        if link_noticia31 != link31 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link31)
            link_noticia31 = link31

#################### TRIGESIMA SEGUNDA NOTICIA ##########################

        page = requests.get("http://www.sabertecnologico.com/categoria/cripito/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='td-module-thumb')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link32 = noticia_name.get('href')
            # print(names)
            print(link32)

        if link_noticia32 != link32 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link32)
            link_noticia32 = link32

#################### TRIGESIMA TERCEIRA NOTICIA ##########################

        page = requests.get("https://canaltech.com.br/criptomoedas/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='col-xs-12 col-sm-6 col-md-4')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link33 = noticia_name.get('href')
            link33= 'https://canaltech.com.br' + link33
            # print(names)
            print(link33)

        if link_noticia33 != link33 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link33)
            link_noticia33 = link33


#################### TRIGESIMA QUARTA NOTICIA ##########################

        page = requests.get("https://cryptowatch.com.br/category/noticias/bitcoin/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post_title entry-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link34 = noticia_name.get('href')

            # print(names)
            print(link34)

        if link_noticia34 != link34 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link34)
            link_noticia34 = link34


#################### TRIGESIMA QUINTA NOTICIA ##########################

        page = requests.get("https://cryptowatch.com.br/category/featured/")
        soup = BeautifulSoup(page.content, 'html.parser')

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='post_title entry-title')
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]
            link35 = noticia_name.get('href')

            # print(names)
            print(link35)

        if link_noticia35 != link35 :
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link35)
            link_noticia35 = link35


#################### TRIGESIMA SEXTA NOTICIA ##########################

        try:
            html = urlopen("https://www.criptomoedasfacil.com/noticias/")
        except HTTPError as e:
            print(e)
        except URLError:
            print("Server down or incorrect domain")
        else:
            res = BeautifulSoup(html.read(), "html5lib")
            tags = res.find("div", {"class": "td-module-thumb"})
            for tag in tags:
                link36 = tag.get('href')
                print(link36)

        if link_noticia36 != link36:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link36)
            link_noticia36 = link36



def pegaUltimaMensagem(msg):
    if msg['text'] == 'envia':
        envia_msg()


#telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(10)
    envia_msg()