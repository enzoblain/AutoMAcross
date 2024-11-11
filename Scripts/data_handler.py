import requests
import pandas as pd

def getForexData(url, apikey, symbol, interval='5min', start_date='None', end_date='None'):
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': apikey,
        start_date: start_date,
        end_date: end_date
    }

    reponse = requests.get(url, params=params)
    data = reponse.json()

    if 'values' in data:
        data = pd.DataFrame(data['values'])
        data.columns = ['timestamp', 'open', 'close', 'min', 'max']
        data['timestamp'] = pd.to_datetime(data['timestamp'])
    else:
        raise ValueError(data['message'])

    return data