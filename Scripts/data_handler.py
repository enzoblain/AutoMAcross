import requests
import pandas as pd

def getForexData(url: str, apikey: str, symbol: str, interval: str ='5min', startDate: str = None, endDate: str = None, timeZone: str = 'Etc/GMT', outputSize: int = 1000) -> pd.DataFrame:
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': apikey,
        'start_date': startDate,
        'end_date': endDate,
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