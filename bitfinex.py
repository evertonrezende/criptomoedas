
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

def coin_detail(coin):
    base_url = 'https://api.bitfinex.com/v1/pubticker/'
    url = '{}{}'.format(base_url, coin)
    response = requests.get(url)
    msg = message(response.json())
    return msg

def message(data):
    last_price = float(data.get('last_price'))
    high_price = float(data.get('high'))
    low_price = float(data.get('low'))
    bid_price = float(data.get('bid'))
    ask_price = float(data.get('ask'))
    timestamp = datetime.fromtimestamp(float(data.get('timestamp')))

    return '''
Last order price: {:,}
Highest trade price of the last 24 hours: {:,}
Lowest trade price of the last 24 hours: {:,}
Innermost bid: {:,}
Innermost ask: {:,}
Timestamp: {}
'''.format(last_price, high_price, low_price, bid_price, ask_price, timestamp)