import requests
import telepot
import json
import time
from bs4 import BeautifulSoup
#import threading



usuariosStartados = []

telegramBot = telepot.Bot('714402433:AAHe96sz7cHwyXFeWRcJdy4JEoRIbFT7Rho')


def mandarMensagem(chat_id, texto):
    # def mandarMensagem(idUsuario, texto):
    telegramBot.sendMessage(chat_id, texto, parse_mode="HTML")
    # telegramBot.sendMessage(idUsuario, texto, parse_mode="HTML")


def envia_msg():
    #telegramUpdates = telegramBot.getUpdates()
    #print(telegramUpdates)
    # idUsuario = telegramUpdates[-1]['message']['chat']['id']
    #chat_id = telegramUpdates[-1]['message']['chat']['378241672']
    chat_id = '-356382448'
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

    while True:
        time.sleep(10)
        page = requests.get("https://www.tradingview.com/markets/cryptocurrencies/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')


    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link = noticia_name.get('href')
            link = 'https://www.tradingview.com' + link
            #print(names)
            print(link)

        if link_noticia != link:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link)
            link_noticia = link

#################### SEGUNDA NOTICIA ##########################
        page = requests.get("https://br.tradingview.com/markets/cryptocurrencies/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link2 = noticia_name.get('href')
            link2 = 'https://br.tradingview.com' + link2
            #print(names)
            print(link2)

        if link_noticia2 != link2:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link2)
            link_noticia2 = link2

#################### TERCEIRA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/BTCUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link3 = noticia_name.get('href')
            link3 = 'https://www.tradingview.com' + link3
            #print(names)
            print(link3)

        if link_noticia3 != link3:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link3)
            link_noticia3 = link3


#################### QUARTA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/ETHUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link4 = noticia_name.get('href')
            link4 = 'https://www.tradingview.com' + link4
            #print(names)
            print(link4)

        if link_noticia4 != link4:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link4)
            link_noticia4 = link4

#################### QUINTA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/XRPUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link5 = noticia_name.get('href')
            link5 = 'https://www.tradingview.com' + link5
            #print(names)
            print(link5)

        if link_noticia5 != link5:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link5)
            link_noticia5 = link5

#################### SEXTA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/EOSUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link6 = noticia_name.get('href')
            link6 = 'https://www.tradingview.com' + link6
            #print(names)
            print(link6)

        if link_noticia6 != link6:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link6)
            link_noticia6 = link6

#################### SETIMA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/LTCUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link7 = noticia_name.get('href')
            link7 = 'https://www.tradingview.com' + link7
            #print(names)
            print(link7)

        if link_noticia7 != link7:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link7)
            link_noticia7 = link7

#################### OITAVA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/XLMUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link8 = noticia_name.get('href')
            link8 = 'https://www.tradingview.com' + link8
            #print(names)
            print(link8)

        if link_noticia8 != link8:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link8)
            link_noticia8 = link8


#################### NONA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/TRXUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link9 = noticia_name.get('href')
            link9 = 'https://www.tradingview.com' + link9
            #print(names)
            print(link9)

        if link_noticia9 != link9:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link9)
            link_noticia9 = link9


#################### DECIMA NOTICIA ##########################
        page = requests.get("https://www.tradingview.com/symbols/ADAUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link10 = noticia_name.get('href')
            link10 = 'https://www.tradingview.com' + link10
            #print(names)
            print(link10)

        if link_noticia10 != link10:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link10)
            link_noticia10 = link10

#################### DECIMA PRIMEIRA ##########################
        page = requests.get("https://www.tradingview.com/symbols/IOTAUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link11 = noticia_name.get('href')
            link11 = 'https://www.tradingview.com' + link11
            #print(names)
            print(link11)

        if link_noticia11 != link11:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link11)
            link_noticia11 = link11

#################### DECIMA SEGUNDA ##########################
        page = requests.get("https://www.tradingview.com/symbols/XMRUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

    # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        #print(noticia_name_list)
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            #names = noticia_name.contents[0]

            link12 = noticia_name.get('href')
            link12 = 'https://www.tradingview.com' + link12
            #print(names)
            print(link12)

        if link_noticia12 != link12:
            #lista_noticia.append(link)
            mandarMensagem(chat_id, link12)
            link_noticia12 = link12

#################### DECIMA TERCEIRA ##########################
        page = requests.get("https://www.tradingview.com/symbols/DASHUSD/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        # print(noticia_name_list)
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]

            link13 = noticia_name.get('href')
            link13 = 'https://www.tradingview.com' + link13
            # print(names)
            print(link13)

        if link_noticia13 != link13:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link13)
            link_noticia13 = link13


#################### DECIMA QUARTA ##########################
        page = requests.get("https://www.tradingview.com/symbols/XBT/ideas/")
        soup = BeautifulSoup(page.content, 'html.parser')
        lista_noticia = []

        # Pegar todo o texto da div BodyText
        noticia_name_list = soup.find(class_='tv-widget-idea__title-row')
        # print(noticia_name_list)
        # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
        noticia_name_list_items = noticia_name_list.find_all('a')
        for noticia_name in noticia_name_list_items:
            # names = noticia_name.contents[0]

            link14 = noticia_name.get('href')
            link14 = 'https://www.tradingview.com' + link14
            # print(names)
            print(link14)

        if link_noticia14 != link14:
            # lista_noticia.append(link)
            mandarMensagem(chat_id, link14)
            link_noticia14 = link14




def pegaUltimaMensagem(msg):
    if msg['text'] == 'envia':
        envia_msg()



#telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(10)
    envia_msg()
    #t = Timer(10)
    #t.start()