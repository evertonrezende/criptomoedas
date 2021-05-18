import json
import requests


header= {'Content-Type':'application/json; charset=utf-8'}
api_btc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BTCUSDT'
btc_var = 'https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1d&limit=250'
api_eth = 'https://api.binance.com/api/v1/ticker/24hr?symbol=ETHUSDT'
api_xrp = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XRPUSDT'
api_bch = 'https://api.binance.com/api/v1/ticker/24hr?symbol=BCCUSDT'
api_eos = 'https://api.binance.com/api/v1/ticker/24hr?symbol=EOSUSDT'
api_xlm = 'https://api.binance.com/api/v1/ticker/24hr?symbol=XLMUSDT'
api_ltc = 'https://api.binance.com/api/v1/ticker/24hr?symbol=LTCUSDT'


def rsi():
        resp_btc= requests.get(btc_var, headers=header)
        a = json.dumps(resp_btc.json())
        b = json.loads(a) #decoode json format
        ab=1 # abertura do candle coletado da API da Binance
        fe=4 # fechamento do candle coletado da API da Binance
        crt=0 #controle de quantos candles vai ler
        #crt_seg= 14 #controle de quantos candles vai ler a partir dos 14 periodos
        list_up= [] #lista dos candles de subida
        list_down= [] # lista dos candles de descida
        #fech_ant= 0  #fechamento anterior 
        periodos= 14
        per_ant= 13
        #chap_charts= 249
        p_ganho_medio= 0 # primeiro ganho médio
        p_perda_medio= 0 # primeira perda média
        l_perda= []
        l_ganho= []
        #ganho_medio= []
        #perda_media= []
        #verifica= 0
        
        
       
        print(b[248][4])
        
 

#bitcoin()    
#etherium()
#ripple()
#bitcoin_cash()
#eos()
#stellar()
#litecoin()
rsi() 

