import json
import requests


header= {'Content-Type':'application/json; charset=utf-8'}
api_btc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BTCUSDT'
btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=4h&limit=250'
api_eth = 'https://api.binance.com/api/v1/ticker/24hr?symbol=ETHUSDT'
api_xrp = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XRPUSDT'
api_bch = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCCUSDT'
api_eos = 'https://api.binance.com/api/v1/ticker/24hr?symbol=EOSUSDT'
api_xlm = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XLMUSDT'
api_ltc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=LTCUSDT'
binance_moedas= 'https://api.binance.com/api/v3/ticker/price'
#api_coinmkt= 'https://api.coinmarketcap.com/v2/ticker/?start=0&limit=10&sort=circulating_supply&structure=array'
api_coinmkt= 'https://api.coinmarketcap.com/v1/ticker/'

def dezmais(): # cria uma lista com as dez primeiras moedas do CoinMarketCap
    resp_coin= requests.get(api_coinmkt, headers=header)
    a = json.dumps(resp_coin.json())
    b = json.loads(a) #decoode json format
    dm= []
    con= 0

    for cont in range(0, 10):
    
        dm.append(b[con]['symbol'])
        con = con+1
    print(f'{dm}')

###################################################################################
def bitcoin():
        resp_btc= requests.get(api_btc, headers=header)
        a = json.dumps(resp_btc.json())
        b = json.loads(a) #decoode json format
        last_price = float(b["lastPrice"])  
        change_percent_price = float(b["priceChangePercent"]) # variação em percentual nas útlimas 24 hrs
        print('BTC: ${:.2f}'.format(last_price) + '-' , '{:.2f}'.format(change_percent_price),'%')  #imprime e converte o numero para duas casas decimais


###################################################################################
def etherium():
        resp_eth= requests.get(api_eth, headers=header)
        a = json.dumps(resp_eth.json())
        b = json.loads(a) #decoode json format
        api_output = float(b["lastPrice"])
        print('ETH: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais

###################################################################################
def ripple():       
    resp_xrp= requests.get(api_xrp, headers=header)
    a = json.dumps(resp_xrp.json())
    b = json.loads(a) #decoode json format
    api_output = float(b["lastPrice"])
    print('XRP: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais
###################################################################################    

def bitcoin_cash():       
    resp_bch= requests.get(api_bch, headers=header)
    a = json.dumps(resp_bch.json())
    b = json.loads(a) #decoode json format
    api_output = float(b["lastPrice"])
    print('BCH: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais
###################################################################################

def eos():       
    resp_eos= requests.get(api_eos, headers=header)
    a = json.dumps(resp_eos.json())
    b = json.loads(a) #decoode json format
    api_output = float(b["lastPrice"])
    print('EOS: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais 
###################################################################################  

def stellar():       
    resp_xlm= requests.get(api_xlm, headers=header)
    a = json.dumps(resp_xlm.json())
    b = json.loads(a) #decoode json format
    api_output = float(b["lastPrice"])
    print('XLM: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais    
###################################################################################
def litecoin():       
    resp_ltc= requests.get(api_ltc, headers=header)
    a = json.dumps(resp_ltc.json())
    b = json.loads(a) #decoode json format
    api_output = float(b["lastPrice"])
    print('LTC: ${:.2f}'.format(api_output))  #imprime e converte o numero para duas casas decimais    
###################################################################################    
def coin():
    bitcoin()
    etherium()
    ripple()
    bitcoin_cash()
    eos()
    stellar()
    litecoin()
    

######################################################################################
def moedas():
        resp_m= requests.get(binance_moedas, headers=header)
        a = json.dumps(resp_m.json())
        b = json.loads(a) #decoode json format
        i= 0
        s= 'symbol'
        temp= []
        temp2= []
        moeda= []
        #ret= "''"
        #print(crp)
        while i < 425:

            temp = (b[i][s])
            moeda.append(temp)
            if format('BTC') in temp: #verifica se existe a string 'BTC' , se tiver adiciona em uma lista
                temp2.append(temp)
            i = i+1


        #print(f'Moedas: {moeda}')   
        print(f'Moedas BTC {temp2}')
        #print(moeda[-1])
###################################################################################
def ma(param_moeda):
    telegramUpdates = telegramBot.getUpdates()
    idUsuario = telegramUpdates[-1]['message']['chat']['id']
    usuariosStartados.append(idUsuario)
    co = 0  # contador para imprimir determinados registros
    ms = []
    periodos = 200
    crt_fe = 0
    fe = 4  # fechamento do candle coletado da API da Binance
    mediaSimples = 0
    for cont in range(0, 5):
        if co == 0:
            tg = '1d'
        elif co == 1:
            tg = '4h'
        elif co == 2:
            tg = '1h'
        elif co == 3:
            tg = '15m'
        elif co == 4:
            tg = '5m'

        btc_var = 'https://api.binance.com/api/v1/klines?symbol=' + param_moeda + 'BTC' '&interval=' + tg + '&limit=200'
        if param_moeda == 'BTC':  # verifica se o usuário digitou BTC e pega o RSI do par BTCUSDT
            btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=' + tg + '&limit=200'

        resp_btc = requests.get(btc_var, headers=header)
        a = json.dumps(resp_btc.json())
        b = json.loads(a)  # decode json format

        fechamento = []

        for cont in range(0, periodos):
            fechamento.append(float(b[crt_fe][fe]))
            crt_fe = crt_fe + 1
            print(crt_fe)

        mediaSimples = sum(fechamento) / 14

        print(mediaSimples)
        #ms.append(rsi_alt)

        co = co + 1

        # print(art[2])
    if param == 'BTC':
        mandarMensagem(idUsuario,
                       '<b>RSI ' + param + '/USDT - BINANCE</b>' + '\n\n' + '1d : ' + ms[0] + '\n' + '4h : ' + ms[
                           1] + '\n' + '1h : ' + ms[2] + '\n' + '15m : ' + ms[3] + '\n' + '5m : ' + ms[4])



def rsi():
        resp_btc= requests.get(btc_var, headers=header)
        a = json.dumps(resp_btc.json())
        b = json.loads(a) #decoode json format
        #ab=1 # abertura do candle coletado da API da Binance


        list_gain= [] #lista dos candles de subida
        list_loss= [] # lista dos candles de descida
        #fech_ant= 0  #fechamento anterior 
        periodos= 14 # são 12 periodos pois o primeiro é igual a zero, começa a contar do zero 
        chap_charts= 250
        #l_perda= []
        #l_ganho= []
        #l_primeira_perda= []
        #l_primeira_alta= []
        ganho_medio= []
        perda_media= []
        rs= []
        rsi= []
        crt=1 # candle após o primeiro
        crt_ant= 0 # primeiro candle na posição 0
        fe=4 # fechamento do candle coletado da API da Binance
        fechamento= []
        crt_fe= 0

        #
        #adiciona o primeiro candle sendo um candle de valor igual a zero pois nao conhecemos se é de alta ou baixa
        #
        list_loss.append(0)
        list_gain.append(0) 

       ############################################################################## 
       #### Criar uma lista com todos os 250 fechamentos ############################
       ##############################################################################
        for cont in range(0, chap_charts):
            fechamento.append(float(b[crt_fe][fe]))
            crt_fe= crt_fe + 1

        print("\n") 
        print(f'Lista fechamentos: {fechamento}')
        print("\n") 
        print(f"QTD candles de fechamento: {len(fechamento)}")

       #######################################################################
       ######## Faz o primeiro tratamento dos 14 primeiros períodos ##########
       #######################################################################
        for cont in range(0, periodos): 
            if float(b[crt_ant][fe]) < float(b[crt][fe]):  #verifica se o candle é alta ou de queda 
                gain= float(b[crt][fe]) - float(b[crt_ant][fe])
                list_gain.append(gain)
                list_loss.append(0) # adicona 0 na lista de loss pois o gain já foi adicionado.

            else:
                loss= float(b[crt_ant][fe]) - float(b[crt][fe])
                list_loss.append(loss) #adiciona na lista pelo preço de fechamento
                list_gain.append(0)

            crt= crt+1   
            crt_ant= crt_ant+1


        p_perda_media= sum(list_loss) /14
        perda_media.append(float(p_perda_media)) #adiciona a primeira perda média na lista

        p_alta_media= sum(list_gain) /14 
        ganho_medio.append(float(p_alta_media)) #adiciona o primeiro ganho médio na lista

        print("\n") 
        print(f'Lista dos valores da primeira perda: {list_loss}')
        print("\n") 
        print(f'Lista dos valores da da primeira alta: {list_gain}') 

        print("\n") 
        print(f'Primeira perda média: {p_perda_media}')
        print("\n") 
        print(f'Primeiro ganho médio: {p_alta_media}')

        print("\n") 
        print(f'CRT_ANT: {crt_ant}')
        print(f'CRT: {crt}')


        ######################################################################
        ######################## Lista de Perda e Ganho ######################
        ######################################################################
        chap_charts= chap_charts-periodos

        for cont in range (0, 235):   

            if float(b[crt_ant][fe]) < float(b[crt][fe]):  #verifica se o candle é alta ou de queda 
                list_loss.append(0)
                gain= float(b[crt][fe]) - float(b[crt_ant][fe])
                list_gain.append(gain)


            else:
                list_gain.append(0)
                loss= float(b[crt_ant][fe]) - float(b[crt][fe]) #adiciona na lista pelo preço de fechamento
                list_loss.append(loss) #adiciona na lista pelo preço de fechamento

            crt= crt+1 
            crt_ant= crt_ant+1

        ####################################################################
        # reseta os contadores para começar a criar a lista de perda e ganho médio
        ####################################################################
        crt_ant= 14
        crt=15

        ##########################################################################
        ## Cria a lista de Ganho médio e perda média
        ##########################################################################
        for cont in range (0, 235):
            pm= float(( (perda_media[-1] * 13) + list_loss[crt]) /14) 
            perda_media.append(float(pm))

            gm= float( ((ganho_medio[-1] * 13) + list_gain[crt]) /14) 
            ganho_medio.append(float(gm))
            crt= crt+1 
            crt_ant= crt_ant+1


        calculo_rs= float(ganho_medio[-1]/perda_media[-1]) #calculo força relativa
        rs.append(float(calculo_rs)) #adiciona rs na lista
        calculo_rsi= 100 - (100/(1+rs[-1])) #calculo rsi
        rsi.append(float(calculo_rsi)) #adiciona rsi na lista





        print("\n") 
        print(f'Lista de GAIN:  {list_gain}')  
        print("\n")  
        print(f'Lista de LOSS:  {list_loss}')  
        print("\n")
        print(f"Lista Perda média: {perda_media}")
        print("\n") 
        print(f"Lista Ganho Médio: {ganho_medio}")
        print("\n") 

        #print(f'Lista RS: {rs}')
        #print("\n")



############################################################################################

        print("\n")
        print (f'RSI: {rsi}')

        print("\n")
        #print (f'Ultimo RSI: {rsi[-1]}')


#bitcoin()    
#etherium()
#ripple()
#bitcoin_cash()
#eos()
#stellar()
#litecoin()
#rsi()

#leitura= input('')
#if leitura == 'coin' or leitura == 'COIN' :
#    coin()
moedas()
#dezmais()
#print("\n")
#print(f'moeda[-1]')
