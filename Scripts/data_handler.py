import requests
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def getForexData(url: str, apikey: str, symbol: str, interval: str ='5min', startDate: str = None, endDate: str = None, timeZone: str = 'Etc/GMT', outputSize: int = 5000) -> pd.DataFrame:
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
        data['Open'] = np.where(data['Open'].astype(float) < data['Close'].astype(float),
                        data['Open'].astype(float) - 0.00006,
                        data['Open'].astype(float) + 0.00006)

        data['High'] = data['High'].astype(float) + 0.00006
        data['Low'] = data['Low'].astype(float) - 0.00006

        data['Close'] = np.where(data['Close'].astype(float) < data['Open'].astype(float),
                                data['Close'].astype(float) - 0.00006,
                                data['Close'].astype(float) + 0.00006)

        data['Timestamp'] = data['Timestamp'].dt.tz_localize('Australia/Sydney').dt.tz_convert(timeZone).dt.tz_localize(None)
    else:
        raise ValueError(data['message'])

    return data

def dataVisualizer(data: pd.DataFrame, n1: int, n2: int, type: str) -> None:
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=data['Timestamp'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    ))

    fig.update_layout(
        title='Trading Graph',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    fig.add_trace(go.Scatter(
        x=data['Timestamp'],
        y=data[f'{n1} Times {type} Average'],
        mode='lines',
        name=f'{n1} Times Global Average',
        line=dict(color='grey', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=data['Timestamp'],
        y=data[f'{n2} Times {type} Average'],
        mode='lines',
        name=f'{n2} Times Global Average',
        line=dict(color='black', width=2)
    ))

    fig.show()