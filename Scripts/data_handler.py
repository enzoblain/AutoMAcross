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
        data = pd.DataFrame(data['values'][::-1])
        data.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data['Open'] = data['Open'].astype(float)
        data['High'] = data['High'].astype(float)
        data['Low'] = data['Low'].astype(float)
        data['Close'] = data['Close'].astype(float)
    else:
        raise ValueError(data['message'])

    return data