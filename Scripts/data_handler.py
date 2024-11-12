import requests
import pandas as pd
import plotly.graph_objects as go

def getForexData(url: str, apikey: str, symbol: str, interval: str, timeZone: str = 'Etc/GMT', outputSize: int = 5000) -> pd.DataFrame:
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': apikey,
        'start_date': None,
        'end_date': None,
        'outputsize': outputSize
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

        data['Timestamp'] = data['Timestamp'].dt.tz_localize('Australia/Sydney').dt.tz_convert(timeZone).dt.tz_localize(None)
    else:
        raise ValueError(data['message'])

    return data