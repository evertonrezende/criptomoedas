import time
import telepot
import json
import requests

usuariosStartados = []

telegramBot = telepot.Bot('468489595:AAHak-3V4uol8oxHyVRpYCj60Usi7Eo0sto')

def mandarMensagem(idUsuario, texto):
    telegramBot.sendMessage(idUsuario, texto, parse_mode="HTML")

def darBoasVindas():
    telegramUpdates= telegramBot.getUpdates()

    primeiroNome= telegramUpdates[-1]['message']['from']['first_name']

    ultimoNome= telegramUpdates[-1]['message']['from']['last_name']

    idUsuario = telegramUpdates[-1]['message']['chat']['id']

    usuariosStartados.append(idUsuario)

    mandarMensagem(idUsuario, 'Seja bem vindo, {0} {1}, se precisar de ajuda digite: ajuda'.format(primeiroNome, ultimoNome))
def help():
    telegramUpdates = telegramBot.getUpdates()

    primeiroNome = telegramUpdates[-1]['message']['from']['first_name']

    ultimoNome = telegramUpdates[-1]['message']['from']['last_name']

    idUsuario = telegramUpdates[-1]['message']['chat']['id']

    usuariosStartados.append(idUsuario)
    mandarMensagem(idUsuario,
                   '<b>ajuda</b>: Solicita ajuda do Robô' +
                   '\n<b>resumo</b>: Mostra o preço das principais moedas na Binance' +
                   '\n<b>rsi moeda</b>: Mostra o RSI de uma moeda na Binance' +
                   '\n<b>ma moeda</b>: Mostra a média de uma moeda na Binance' +
                   '\n<b>arb moeda</b>: Exibe preço atual, melhor venda e melhor compra. ' +
                   '\n<b>coin nome_moeda</b>: Mostra os dados de uma moeda. ' +
                   '\n<b>adx</b>: Mostra o ADX de uma moeda')


def darBoasVindas():

    telegramUpdates= telegramBot.getUpdates()
    primeiroNome= telegramUpdates[-1]['message']['from']['first_name']
    ultimoNome= telegramUpdates[-1]['message']['from']['last_name']
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)
    mandarMensagem(idUsuario, 'Bem vindo {0} {1}, se precisar de ajuda digite: <b>ajuda</b>'.format(primeiroNome, ultimoNome))





def ma_tradingview(param):
    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)



    #if param == 'BTC':
    market = param + 'USDT'
    print(market)
    #else:
     #   market = param + 'BTC'
     #   print(market)
    co_ma = 0  # contador para imprimir determinados registros
    co_li = 0
    lim = 0
    sma_1 = []
    sma_2 = []
    sma_3 = []
    #sma_4 = []



    lim = '200'

    # for cont in range(0, 2):
    # if co_ma == 0:
    candle = '1d'  # candle de 1 dia
    # f = "SMA" + lim

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    url = "https://scanner.tradingview.com/crypto/scan"
    payload = {

        "symbols": {
            "tickers": ["BINANCE:{}".format(market)],
            "query": {"types": []}
        },
        "columns": [

            "RSI".format(candle)
            # "Stoch.K".format(candle),
            # "ADX".format(candle),
            # "CCI20".format(candle),
            # "BB.upper".format(candle),
            # "BB.lower".format(candle),
            # "ATR".format(candle),
            # "AO|{}".format(candle),
            # "MACD.macd".format(candle),
            # "MACD.signal".format(candle),
            # "Mom".format(candle),
            # "SMA20".format(candle),
            # "SMA50".format(candle),
            # "SMA100".format(candle),
            # "SMA200".format(candle),
            # "EMA20".format(candle),
            # "EMA50".format(candle),
            # "EMA100".format(candle),
            # "EMA200".format(candle)
        ]
    }
    print(payload)
    resp = requests.post(url, headers=headers, data=json.dumps(payload)).json()
    indicador = resp["data"][0]["d"]
    print(resp)




def pegaUltimaMensagem(msg):

    if msg['text'] == '/start':
        darBoasVindas()


    elif msg['text'].find('sma') != -1 or msg['text'].find('SMA') != -1:
        ma_moeda = msg['text']
        ma_moeda = ma_moeda[3:10]
        ma_moeda = ma_moeda.upper()
        print(ma_moeda)
        ma_tradingview(ma_moeda)




telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(1)