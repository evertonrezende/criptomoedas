import requests, json, time, datetime


def mlog(market, *text):
    text = [str(i) for i in text]
    text = " ".join(text)

    datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

    print("[{} {}] - {}".format(datestamp, market, text))

def get_signal(candle):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    url = "https://scanner.tradingview.com/crypto/scan"



    payload = {

        "filter": [{"left": "RSI", "operation": "nempty"},
                   {"left": "exchange", "operation": "equal", "right": "BINANCE"},
                   {"left": "name,description", "operation": "match", "right": "BTC"}],


        "columns":

            ["name", "RSI|{}".format(candle)],
            "sort": {"sortBy": "RSI", "sortOrder": "asc"},
            "options": {"lang": "pt"},
            "range": [0, 10]
     }


    resp = requests.post(url, headers=headers, data=json.dumps(payload)).json()
    print(resp)
    n= 0
    n_rsi = []
    v_rsi = []
    for cont in range(0, 10):
        moeda_name = resp["data"][n]["d"][0]
        moeda_price = resp["data"][n]["d"][1]
        n_rsi.append(moeda_name)
        v_rsi.append(moeda_price)
        #print(moeda_name)
        #print(moeda_price)
        n = n+1

    print(n_rsi[0], v_rsi[0])
    print(n_rsi[1], v_rsi[1])
    print(n_rsi[2], v_rsi[2])
    print(n_rsi[3], v_rsi[3])
    print(n_rsi[4], v_rsi[4])
    print(n_rsi[5], v_rsi[5])
    print(n_rsi[6], v_rsi[6])
    print(n_rsi[7], v_rsi[7])
    print(n_rsi[8], v_rsi[8])
    print(n_rsi[9], v_rsi[9])

    #return signal


if __name__ == "__main__":

    market = "BTCUSDT"
    candle = '240'  # Represented in minutes

    #mlog(market, "Getting TV signal for {}, {} minute candle.".format(market, candle))
    signal = get_signal(candle)
    #mlog(market, signal)