import telepot
import json
import requests
import time

header = {'Content-Type': 'application/json; charset=utf-8'}
api_coinmkt = 'https://api.coinmarketcap.com/v1/ticker/'
api_btc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BTCUSDT'
#api_eth = 'https://api.binance.com/api/v1/ticker/24hr?symbol=ETHUSDT'
#api_xrp = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XRPUSDT'
#api_bch = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCCUSDT'
#api_eos = 'https://api.binance.com/api/v1/ticker/24hr?symbol=EOSUSDT'
#api_xlm = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XLMUSDT'
#api_ltc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=LTCUSDT'
#api_bchabc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCHABCUSDT'
#api_bchsv = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCHSVUSDT'
#api_bchsv = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCHSVUSDT'
#api_trx = 'https://api.binance.com/api/v1/ticker/24hr?symbol=TRXUSDT'
#api_ada = 'https://api.binance.com/api/v1/ticker/24hr?symbol=ADAUSDT'


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

def moedas_binance():

    binance_moedas = 'https://api.binance.com/api/v3/ticker/price'
    resp_m = requests.get(binance_moedas, headers=header)
    a = json.dumps(resp_m.json())
    b = json.loads(a)  # decoode json format
    i = 0
    s = 'symbol'
    temp = []
    temp2 = []
    moeda = []
    # ret= "''"
    # print(crp)
    while i < 425:

          temp = (b[i][s])
          moeda.append(temp)
          if format('BTC') in temp:  # verifica se existe a string 'BTC' , se tiver adiciona em uma lista
                temp2.append(temp)
          i = i + 1


    print(f'Moedas BTC {temp2}')


def coin(param):

    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)

    ap = 'https://api.coinmarketcap.com/v1/ticker/' + param
    resp_coinmkt = requests.get(ap, headers=header)
    a = json.dumps(resp_coinmkt.json())
    b = json.loads(a)

    vol24 = float(b[0]["24h_volume_usd"])
    rank= b[0]["rank"]
    name= b[0]["name"]
    symbol= b[0]["symbol"]
    per1h = float(b[0]["percent_change_1h"])
    per7d = float(b[0]["percent_change_7d"])
    per24h = float(b[0]["percent_change_24h"])
    price_usd = float(b[0]["price_usd"])
    price_btc = b[0]["price_btc"]

    mandarMensagem(idUsuario, '<b>coinmarketcap.com - USD</b>' + '\n\n' +
                              '<b> Nome: </b> ' + name + '\n' +
                              '<b> Símbolo: </b> ' + symbol + '\n' +
                              '<b> Rank </b>:' + rank + '\n' +
                              '<b> Preço em USD: </b> ${:.2f}'.format(price_usd) + '\n' +
                              '<b> Preço em BTC:  </b>' + price_btc + '\n' +
                              '<b> Volume (24h):  </b> {:.2f}'.format(vol24) + '\n' +
                              '<b> Variação (1h):  </b> {:.2f}'.format(per1h) + '%' + '\n' +
                              '<b> Variação (24h):  </b> {:.2f}'.format(per24h) + '%' + '\n' +
                              '<b> Variação (7d):  </b> {:.2f}'.format(per7d) + '%'

                   )

def bitcoin():

    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)

    l_mo = []
    cont = 0
    api_coinmkt = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'
    resp_coinmkt = requests.get(api_coinmkt, headers=header)
    a = json.dumps(resp_coinmkt.json())
    b = json.loads(a)

    price1 = float(b[0]['price_usd'])
    pc24_1 = float(b[0]['percent_change_24h'])

    price2 = float(b[1]['price_usd'])
    pc24_2 = float(b[1]['percent_change_24h'])

    price3 = float(b[2]['price_usd'])
    pc24_3 = float(b[2]['percent_change_24h'])

    price4 = float(b[3]['price_usd'])
    pc24_4 = float(b[3]['percent_change_24h'])

    price5 = float(b[4]['price_usd'])
    pc24_5 = float(b[4]['percent_change_24h'])

    price6 = float(b[5]['price_usd'])
    pc24_6 = float(b[5]['percent_change_24h'])

    price7 = float(b[6]['price_usd'])
    pc24_7 = float(b[6]['percent_change_24h'])

    price8 = float(b[7]['price_usd'])
    pc24_8 = float(b[7]['percent_change_24h'])

    price9 = float(b[8]['price_usd'])
    pc24_9 = float(b[8]['percent_change_24h'])

    price10 = float(b[9]['price_usd'])
    pc24_10 = float(b[9]['percent_change_24h'])
    #print(price10)


    for cont in range(0, 10):
        mo_binance = b[cont]['symbol']
        l_mo.append(mo_binance)
        cont = cont + 1
    print(l_mo)



    #resp_btc = requests.get(api_btc, headers=header)
    #a = json.dumps(resp_btc.json())
    #b = json.loads(a)  # decoode json format
    #last_price = float(b["lastPrice"])s
    #change_percent_price = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs



    #resp_eth = requests.get(api_eth, headers=header)
    #a = json.dumps(resp_eth.json())
    #b = json.loads(a)  # decoode json format
    #last_price_eth = float(b["lastPrice"])
    #change_percent_price_eth = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs


    #resp_xrp= requests.get(api_xrp, headers=header)
    #a = json.dumps(resp_xrp.json())
    #b = json.loads(a) #decoode json format
    #last_price_xrp = float(b["lastPrice"])
    #change_percent_price_xrp = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs


    #resp_xlm= requests.get(api_xlm, headers=header)
    #a = json.dumps(resp_xlm.json())
    #b = json.loads(a) #decoode json format
    #last_price_xlm = float(b["lastPrice"])
    #change_percent_price_xlm = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs
    #mandarMensagem(idUsuario, 'BCH: ${:.2f}'.format(last_price_bch) + ' (' + '{:.2f}'.format(change_percent_price_bch) + '%' + ')')

    #resp_eos= requests.get(api_eos, headers=header)
    #a = json.dumps(resp_eos.json())
    #b = json.loads(a) #decoode json format
    #last_price_eos = float(b["lastPrice"])
    #change_percent_price_eos = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

    #resp_ltc = requests.get(api_ltc, headers=header)
    #a = json.dumps(resp_ltc.json())
    #b = json.loads(a)  # decoode json format
    #last_price_ltc = float(b["lastPrice"])
    #change_percent_price_ltc = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

    #resp_bchsv = requests.get(api_bchsv, headers=header)
    #a = json.dumps(resp_bchsv.json())
    #b = json.loads(a)  # decoode json format
    #last_price_bchsv = float(b["lastPrice"])
    #change_percent_price_bchsv = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

   #resp_bchabc = requests.get(api_bchabc, headers=header)
    #a = json.dumps(resp_bchabc.json())
    #b = json.loads(a)  # decoode json format
    #last_price_bchabc = float(b["lastPrice"])
    #change_percent_price_bchabc = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

    #resp_trx = requests.get(api_trx, headers=header)
   ##a = json.dumps(resp_trx.json())
    #b = json.loads(a)  # decoode json format
   # last_price_trx = float(b["lastPrice"])
    #change_percent_price_trx = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

    #resp_ada = requests.get(api_ada, headers=header)
    #a = json.dumps(resp_ada.json())
    #b = json.loads(a)  # decoode json format
    #last_price_ada = float(b["lastPrice"])
    #change_percent_price_ada = float(b["priceChangePercent"])  # variação em percentual nas útlimas 24 hrs

    mandarMensagem(idUsuario, '<b>coinmarketcap.com - USD</b>' + '\n\n' +
                              '<b>' + l_mo[0] + '</b>: ${:.2f}'.format(price1) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_1) + '%' + ')' + '\n' +
                              '<b>' + l_mo[1] + '</b>: ${:.2f}'.format(price2) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_2) + '%' + ')' + '\n' +
                              '<b>' + l_mo[2] + '</b>: ${:.2f}'.format(price3) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_3) + '%' + ')' + '\n' +
                              '<b>' + l_mo[3] + '</b>: ${:.2f}'.format(price4) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_4) + '%' + ')' + '\n' +
                              '<b>' + l_mo[4] + '</b>: ${:.2f}'.format(price5) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_5) + '%' + ')' + '\n' +
                              '<b>' + l_mo[5] + '</b>: ${:.2f}'.format(price6) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_6) + '%' + ')' + '\n' +
                              '<b>' + l_mo[6] + '</b>: ${:.2f}'.format(price7) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_7) + '%' + ')' + '\n' +
                              '<b>' + l_mo[7] + '</b>: ${:.2f}'.format(price8) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_8) + '%' + ')' + '\n' +
                              '<b>' + l_mo[8] + '</b>: ${:.2f}'.format(price9) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_9) + '%' + ')' + '\n' +
                              '<b>' + l_mo[9] + '</b>: ${:.2f}'.format(price10) + ' | ' + '24h:' + ' (' + '{:.2f}'.format(pc24_10) + '%' + ')'
                   )

def compara(param):

    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)

    moeda_binance = 'https://api.binance.com/api/v1/ticker/24hr?symbol=' + param.upper() + 'USDT'
    #print(moeda_binance)
    resp_btc_binance = requests.get(moeda_binance, headers=header)
    a = json.dumps(resp_btc_binance.json())
    b = json.loads(a)
    last_price_binance = float(b["lastPrice"])
    ask_binance = float(b["askPrice"])
    bid_binance = float(b["bidPrice"])

    moeda_bitfinex = 'https://api.bitfinex.com/v1/pubticker/' + param + 'usd'
    #print(moeda_bitfinex)
    resp_btc_bitfinex = requests.get(moeda_bitfinex, headers=header)
    a = json.dumps(resp_btc_bitfinex.json())
    b = json.loads(a)
    last_price_bitfinex = float(b["last_price"])
    ask_bitfinex = float(b["ask"])
    bid_bitfinex = float(b["bid"])

############################################################################################################
    #moeda_bittrex = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-' + param
    moeda_bittrex = 'https://bittrex.com/api/v1.1/public/getticker?market=usdt-' + param
    #print(moeda_bittrex)
    resp_btc_bittrex = requests.get(moeda_bittrex, headers=header)
    a = json.dumps(resp_btc_bittrex.json())
    b = json.loads(a)
    last_price_bittrex = float(b["result"]["Last"])
    ask_bittrex = float(b["result"]["Ask"])
    bid_bittrex = float(b["result"]["Bid"])
    #print(f'Close: {b["Last"]}')
    #print(last_price_bittrex)
    #print(f' Bid: {b["result"]["0"]["Bid"]}')

####################################################################################
    moeda_huobi = 'http://api.huobi.com/market/detail/merged?&symbol=' + param + 'usdt'
    #print(moeda_huobi)
    resp_btc_huobi = requests.get(moeda_huobi, headers=header)
    a = json.dumps(resp_btc_huobi.json())
    b = json.loads(a)
    last_price_huobi = b["tick"]["close"]
    ask_huobi = b["tick"]["ask"]
    bid_huobi = b["tick"]["bid"]
    #print(f'Close: {last_price_huobi}')
    #print(f' Ask: {ask_huobi[0]}')
    #print(f' Bid: {bid_huobi[0]}')

    ####################################################################################
    moeda_poloniex = 'https://poloniex.com/public?command=returnTicker'
    print(moeda_poloniex)
    resp_btc_poloniex = requests.get(moeda_poloniex, headers=header)
    a = json.dumps(resp_btc_poloniex.json())
    b = json.loads(a)
    last_price_poloniex = float(b["USDT_BTC"]["last"])
    ask_poloniex = float(b["USDT_BTC"]["lowestAsk"])
    bid_poloniex = float(b["USDT_BTC"]["highestBid"])
    print(last_price_poloniex)

###########################################################################################
    moeda_hitbtc = 'https://api.hitbtc.com/api/2/public/ticker/' + param.upper() + 'USD'
    #print(moeda_hitbtc)
    resp_btc_hitbtc = requests.get(moeda_hitbtc, headers=header)
    a = json.dumps(resp_btc_hitbtc.json())
    b = json.loads(a)
    last_price_hitbtc = float(b["last"])
    ask_hitbtc = float(b["ask"])
    bid_hitbtc = float(b["bid"])
    #print(f'Close Hitbtc: {last_price_hitbtc}')
    #print(f' Ask: {ask_hitbtc}')
    #print(f' Bid: {bid_hitbtc}')
###############################################################################################################



    mandarMensagem(idUsuario, '<b>BINANCE - ' + param.upper() + '/USDT </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_binance) + '\n' +
                              'Ask : ${:.4f}'.format(ask_binance) + '\n' +
                              'Bid : ${:.4f}'.format(bid_binance) + '\n' +
                              '<b>BITFINEX - ' + param.upper() + '/USD </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_bitfinex) + '\n' +
                              'Ask : ${:.4f}'.format(ask_bitfinex) + '\n' +
                              'Bid : ${:.4f}'.format(bid_bitfinex) + '\n' +
                              '<b>HUOBI - ' + param.upper() + '/USDT </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_huobi) + '\n' +
                              'Ask : ${:.4f}'.format(ask_huobi[0]) + '\n' +
                              'Bid : ${:.4f}'.format(bid_huobi[0]) + '\n' +
                              '<b>BITTREX - ' + param.upper() + '/USDT </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_bittrex) + '\n' +
                              'Ask : ${:.4f}'.format(ask_bittrex) + '\n' +
                              'Bid : ${:.4f}'.format(bid_bittrex) + '\n' +
                              '<b>POLONIEX - ' + param.upper() + '/USDT </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_poloniex) + '\n' +
                              'Ask : ${:.4f}'.format(ask_poloniex) + '\n' +
                              'Bid : ${:.4f}'.format(bid_poloniex) + '\n' +
                              '<b>HITBTC - ' + param.upper() + '/USD </b>' + '\n' +
                              'Último preço : ${:.4f}'.format(last_price_hitbtc) + '\n' +
                              'Ask : ${:.4f}'.format(ask_hitbtc) + '\n' +
                              'Bid : ${:.4f}'.format(bid_hitbtc)
                   )

def rsi(param):
    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)
    art = []
    co= 0 # contador para imprimir determinados registros
    for cont in range(0, 5):
        if co == 0 :
            tg= '1d'
        elif co == 1 :
            tg= '4h'
        elif co == 2 :
            tg = '1h'
        elif co == 3 :
            tg = '15m'
        elif co ==4 :
            tg = '5m'

        btc_var = 'https://api.binance.com/api/v1/klines?symbol=' + param + 'BTC' '&interval=' + tg + '&limit=250'
        if param == 'BTC': #verifica se o usuário digitou BTC e pega o RSI do par BTCUSDT
            btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=' + tg + '&limit=250'


        resp_btc = requests.get(btc_var, headers=header)
        a = json.dumps(resp_btc.json())
        b = json.loads(a)  # decode json format

        list_gain = []  # lista dos candles de subida
        list_loss = []  # lista dos candles de descida
        # fech_ant= 0  #fechamento anterior
        periodos = 14  # são 12 periodos pois o primeiro é igual a zero, começa a contar do zero
        chap_charts = 250
        ganho_medio = []
        perda_media = []
        rs = []
        rsi = []
        crt = 1  # candle após o primeiro
        crt_ant = 0  # primeiro candle na posição 0
        fe = 4  # fechamento do candle coletado da API da Binance
        fechamento = []
        crt_fe = 0

        #
        # adiciona o primeiro candle sendo um candle de valor igual a zero pois nao conhecemos se é de alta ou baixa
        #
        list_loss.append(0)
        list_gain.append(0)

        ##############################################################################
        #### Criar uma lista com todos os 250 fechamentos ############################
        ##############################################################################
        for cont in range(0, chap_charts):
            fechamento.append(float(b[crt_fe][fe]))
            crt_fe = crt_fe + 1

        #######################################################################
        ######## Faz o primeiro tratamento dos 14 primeiros períodos ##########
        #######################################################################
        for cont in range(0, periodos):
            if float(b[crt_ant][fe]) < float(b[crt][fe]):  # verifica se o candle é alta ou de queda
                gain = float(b[crt][fe]) - float(b[crt_ant][fe])
                list_gain.append(gain)
                list_loss.append(0)  # adicona 0 na lista de loss pois o gain já foi adicionado.

            else:
                loss = float(b[crt_ant][fe]) - float(b[crt][fe])
                list_loss.append(loss)  # adiciona na lista pelo preço de fechamento
                list_gain.append(0)

            crt = crt + 1
            crt_ant = crt_ant + 1
        p_perda_media = sum(list_loss) / 14
        perda_media.append(float(p_perda_media))  # adiciona a primeira perda média na lista

        p_alta_media = sum(list_gain) / 14
        ganho_medio.append(float(p_alta_media))  # adiciona o primeiro ganho médio na lista

        ######################################################################
        ######################## Lista de Perda e Ganho ######################
        ######################################################################
        chap_charts = chap_charts - periodos

        for cont in range(0, 235):

            if float(b[crt_ant][fe]) < float(b[crt][fe]):  # verifica se o candle é alta ou de queda
                list_loss.append(0)
                gain = float(b[crt][fe]) - float(b[crt_ant][fe])
                list_gain.append(gain)


            else:
                list_gain.append(0)
                loss = float(b[crt_ant][fe]) - float(b[crt][fe])  # adiciona na lista pelo preço de fechamento
                list_loss.append(loss)  # adiciona na lista pelo preço de fechamento

            crt = crt + 1
            crt_ant = crt_ant + 1

        ####################################################################
        # reseta os contadores para começar a criar a lista de perda e ganho médio
        ####################################################################
        crt_ant = 14
        crt = 15

        ##########################################################################
        ## Cria a lista de Ganho médio e perda média
        ##########################################################################
        for cont in range(0, 235):
            pm = float(((perda_media[-1] * 13) + list_loss[crt]) / 14)
            perda_media.append(float(pm))

            gm = float(((ganho_medio[-1] * 13) + list_gain[crt]) / 14)
            ganho_medio.append(float(gm))
            crt = crt + 1
            crt_ant = crt_ant + 1

        calculo_rs = float(ganho_medio[-1] / perda_media[-1])  # calculo força relativa
        rs.append(float(calculo_rs))  # adiciona rs na lista
        calculo_rsi = 100 - (100 / (1 + rs[-1]))  # calculo rsi
        rsi.append(float(calculo_rsi))  # adiciona rsi na lista

        rsi = str(rsi)  # converte numero para string para imprimir somente os 6 primeiros digitos

        rsi_alt = rsi[1:6]
        print(rsi_alt)

        art.append(rsi_alt)

        co = co + 1

    #print(art[2])
    if param == 'BTC':
        mandarMensagem(idUsuario, '<b>RSI ' + param + '/USDT - BINANCE</b>' + '\n\n' + '1d : ' + art[0] + '\n' +
                       '4h : ' + art[1] + '\n' +
                       '1h : ' + art[2] + '\n' +
                       '15m : ' + art[3] + '\n' +
                       '5m : ' + art[4])
    else:
        mandarMensagem(idUsuario, '<b>RSI ' + param + '/BTC - BINANCE</b>' + '\n\n' + '1d : ' + art[0] + '\n' +
                       '4h : ' + art[1] + '\n' +
                       '1h : ' + art[2] + '\n' +
                       '15m : ' + art[3] + '\n' +
                       '5m : ' + art[4])
        #mandarMensagem(idUsuario, '<b>bold</b>')

def ma(param_moeda):
    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)
    periodos = 100
    sma_1 = []
    sma_2 = []
    sma_3 = []
    sma_4 = []
    mediaSimples = 0
    co_ma = 0  # contador para imprimir determinados registros
    co_li = 0
    lim = 0
    for cont in range(0, 4):
            if co_li == 0:
                lim = '200'
            elif co_li == 1:
                lim = '100'
                co_ma = 0
            elif co_li == 2:
                lim = '21'
                co_ma = 0
            elif co_li == 3:
                lim = '9'
                co_ma = 0

            for cont in range(0, 3):
                if co_ma == 0:
                    tg = '1d'
                elif co_ma == 1:
                    tg = '4h'
                elif co_ma == 2:
                    tg = '1h'

                btc_var = 'https://api.binance.com/api/v1/klines?symbol=' + param_moeda + 'BTC' '&interval=' + tg + '&limit=' + lim
                if param_moeda == 'BTC':  # verifica se o usuário digitou BTC e pega o RSI do par BTCUSDT
                    btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=' + tg + '&limit=' + lim

                resp_btc = requests.get(btc_var, headers=header)
                a = json.dumps(resp_btc.json())
                b = json.loads(a)  # decode json format

                crt_fe = 0
                fe = 4  # fechamento do candle coletado da API da Binance
                soma_price = 0
                fechamento = []
                ms = []
                for cont in range(0, int(lim)):
                    price = float(b[crt_fe][fe])
                    fechamento.append(price)

                    #print(fechamento)
                    soma_price= soma_price + price
                    crt_fe = crt_fe + 1

                mediaSimples = float(soma_price / int(lim))

                #print(f'Media simples: {mediaSimples}')
                ms.append(float(mediaSimples))

                ms = str(ms)
                ms_alt = ms[1:8]
                #ms_alt = float(ms_alt)
                #print(ms_alt)
                if lim == '200':
                    sma_1.append(ms_alt)
                elif lim == '100':
                    sma_2.append(ms_alt)
                elif lim == '21':
                    sma_3.append(ms_alt)
                elif lim == '9':
                    sma_4.append(ms_alt)
                co_ma = co_ma + 1


            co_li = co_li + 1

    if param_moeda == 'BTC':
        mandarMensagem(idUsuario, '<b>SMA ' + '(200 períodos) ' + param_moeda + '/USDT - BINANCE</b>' + '\n' + '1d : ' + sma_1[0] +
                   '\n' + '4h : ' + sma_1[1] +
                   '\n' + '1h : ' + sma_1[2] + '\n' +
                       '<b>SMA ' + '(100 períodos) ' + param_moeda + '/USDT - BINANCE</b>' + '\n' +
                       '1d : ' + sma_2[0] + '\n' +
                       '4h : ' + sma_2[1] + '\n' +
                       '1h : ' + sma_2[2] + '\n' +
                       '<b>SMA ' + '(21 períodos) ' + param_moeda + '/USDT - BINANCE</b>' + '\n' +
                       '1d : ' + sma_3[0] + '\n' +
                       '4h : ' + sma_3[1] + '\n' +
                       '1h : ' + sma_3[2] + '\n' +
                        '<b>SMA ' + '(9 períodos) ' + param_moeda + '/USDT - BINANCE</b>' + '\n' +
                        '1d : ' + sma_4[0] + '\n' +
                        '4h : ' + sma_4[1] + '\n' +
                        '1h : ' + sma_4[2] + '\n')

    else:
        mandarMensagem(idUsuario, '<b>SMA ' + '(200 períodos) ' + param_moeda + '/BTC - BINANCE</b>' + '\n' + '1d : ' + sma_1[0] +
                   '\n' + '4h : ' + sma_1[1] +
                   '\n' + '1h : ' + sma_1[2] + '\n' +
                       '<b>SMA ' + '(100 períodos) ' + param_moeda + '/BTC - BINANCE</b>' + '\n' +
                       '1d : ' + sma_2[0] + '\n' +
                       '4h : ' + sma_2[1] + '\n' +
                       '1h : ' + sma_2[2] + '\n' +
                       '<b>SMA ' + '(21 períodos) ' + param_moeda + '/BTC - BINANCE</b>' + '\n' +
                       '1d : ' + sma_3[0] + '\n' +
                       '4h : ' + sma_3[1] + '\n' +
                       '1h : ' + sma_3[2] + '\n' +
                        '<b>SMA ' + '(9 períodos) ' + param_moeda + '/BTC - BINANCE</b>' + '\n' +
                        '1d : ' + sma_4[0] + '\n' +
                        '4h : ' + sma_4[1] + '\n' +
                        '1h : ' + sma_4[2] + '\n')

def ema(param_moeda):
    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)
    periodos = 100
    sma_1 = []
    sma_2 = []
    sma_3 = []
    sma_4 = []
    mediaSimples = 0
    co_ma = 0  # contador para imprimir determinados registros
    co_li = 0
    lim = 0
    for cont in range(0, 4):
            if co_li == 0:
                lim = '200'
            elif co_li == 1:
                lim = '100'
                co_ma = 0
            elif co_li == 2:
                lim = '21'
                co_ma = 0
            elif co_li == 3:
                lim = '9'
                co_ma = 0

            for cont in range(0, 3):
                if co_ma == 0:
                    tg = '1d'
                elif co_ma == 1:
                    tg = '4h'
                elif co_ma == 2:
                    tg = '1h'

                btc_var = 'https://api.binance.com/api/v1/klines?symbol=' + param_moeda + 'BTC' '&interval=' + tg + '&limit=' + lim
                if param_moeda == 'BTC':  # verifica se o usuário digitou BTC e pega o RSI do par BTCUSDT
                    btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=' + tg + '&limit=' + lim

                resp_btc = requests.get(btc_var, headers=header)
                a = json.dumps(resp_btc.json())
                b = json.loads(a)  # decode json format

                crt_fe = 0
                fe = 4  # fechamento do candle coletado da API da Binance
                soma_price = 0
                fechamento = []
                ms = []
                for cont in range(0, int(lim)):
                    price = float(b[crt_fe][fe])
                    fechamento.append(price)

                    #print(fechamento)
                    soma_price= soma_price + price
                    crt_fe = crt_fe + 1

                mediaSimples = float(soma_price / int(lim))

                #print(f'Media simples: {mediaSimples}')
                ms.append(float(mediaSimples))

                ms = str(ms)
                ms_alt = ms[1:8]
                #print(ms_alt)
                if lim == '200':
                    sma_1.append(ms_alt)

                    multiplicador = 0.0099
                    print(multiplicador)
                    ema_1 = (float(sma_1[0]) * float(multiplicador)) + float(sma_1[0])
                    print(f'EMA 1d: {ema_1}')

                elif lim == '100':
                    sma_2.append(ms_alt)
                elif lim == '21':
                    sma_3.append(ms_alt)
                elif lim == '9':
                    sma_4.append(ms_alt)
                co_ma = co_ma + 1


            co_li = co_li + 1


def pegaUltimaMensagem(msg):

    if msg['text'] == '/start':
        darBoasVindas()


    elif msg['text'] == 'resumo' or msg['text'] == 'RESUMO':

        bitcoin()

    elif msg['text'] == 'ajuda' or msg['text'] == 'AJUDA':
        help()

    elif msg['text'].find('coin') != -1 or msg['text'].find('COIN') != -1:
        coin_mk = msg['text']
        coin_mk = coin_mk[5:12]
        print(coin_mk)
        coin(coin_mk)

    elif msg['text'].find('ma') != -1 or msg['text'].find('MA') != -1:
        ma_moeda = msg['text']
        ma_moeda = ma_moeda[3:10]
        ma_moeda = ma_moeda.upper()
        print(ma_moeda)
        ma(ma_moeda)

    elif msg['text'].find('em') != -1 or msg['text'].find('EM') != -1:
        ma_moeda = msg['text']
        ma_moeda = ma_moeda[3:10]
        ma_moeda = ma_moeda.upper()
        print(ma_moeda)
        ema(ma_moeda)

    elif msg['text'].find('rsi') != -1 or msg['text'].find('RSI') != -1:
        modif = msg['text']
        modif = modif[4:10]
        modif = modif.upper()
        print(modif)
        rsi(modif)

    elif msg['text'].find('1d') != -1 or msg['text'].find('1d') != -1:
        modif = msg['text']
        modif = modif[4:10]
        modif = modif.upper()
        print(modif)
        rsi(modif)

    elif msg['text'].find('arb') != -1 or msg['text'].find('ARB') != -1:
        modif = msg['text']
        modif = modif[4:10]
        #modif = modif.upper()
        print(modif)
        compara(modif)
    # else:
    # telegramUpdates = telegramBot.getUpdates()
    # idUsuario = telegramUpdates[-1]['message']['chat']['id']
    # usuariosStartados.append(idUsuario)
    # mandarMensagem(idUsuario,'Comando inválido, se precisar de ajuda digite: /ajuda')


telegramBot.message_loop(pegaUltimaMensagem)

while True:
    time.sleep(1)