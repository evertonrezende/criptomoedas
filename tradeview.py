import requests, json


def get_signal(market, candle):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    url = "https://scanner.tradingview.com/crypto/scan"
    payload =   {


                    "symbols": {
                        "tickers": ["BINANCE:{}".format(market)],
                        "query": { "types": [] }
                    },
                    "columns": [

                        "RSI".format(candle)
                        #"Stoch.K".format(candle),
                        #"ADX".format(candle),
                        #"CCI20".format(candle),
                        #"BB.upper".format(candle),
                        #"BB.lower".format(candle),
                        #"ATR".format(candle),
                        #"AO|{}".format(candle),
                        #"MACD.macd".format(candle),
                        #"MACD.signal".format(candle),
                        #"Mom".format(candle),
                        #"SMA20".format(candle),
                        #"SMA50".format(candle),
                        #"SMA100".format(candle),
                        #"SMA200".format(candle),
                        #"EMA20".format(candle),
                        #"EMA50".format(candle),
                        #"EMA100".format(candle),
                        #"EMA200".format(candle)
                    ]
                }
    print(payload)
    resp = requests.post(url,headers=headers,data=json.dumps(payload)).json()
    indicador = resp["data"][0]["d"]
    print(resp)
    #print(f'RSI: {indicador[0]}') #RSI 14 periodos
    #print(f'Estocastico %K: {indicador[1]}')  #Quando a linha %K cruza acima de 50 é dado um sinal de compra e no contrario venda
    #print(f'ADX: {indicador[2]}')
    #print(f'CCI20: {indicador[3]}') # Valores +100 significam sobrecompra e valores -100 significam sobrevenda
    #print(f'BB Superior: {indicador[4]}')
    #print(f'BB Inferior: {indicador[5]}')
    #print(f'ATR: {indicador[6]}') #Media de Range Verdadeiro (14)
   # print(f'AO: {indicador[7]}') #Oscilador Extraordinario
    #print(f'Nível MACD (12,26): {indicador[8]}')
    #print(f'Sinal MACD (12,26): {indicador[9]}')
    #print(f'Momentum (10) {indicador[10]}')
    print(f'SMA20 {indicador[0]}')
    #print(f'SMA50 {indicador[12]}')
    #print(f'SMA100 {indicador[13]}')
    #print(f'SMA200 {indicador[14]}')
    #print(f'EMA20 {indicador[15]}')
    #print(f'EMA50 {indicador[16]}')
    #print(f'EMA100 {indicador[17]}')
    #print(f'EMA200 {indicador[18]}')

if __name__ == "__main__":

    market = "BTCUSDT"
    candle = '1d' #Represented in minutes ou 1d , 1W ou 1M

    get_signal(market, candle)