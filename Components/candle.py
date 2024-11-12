import pandas as pd
import numpy as np
    
def filterCandles(candles: pd.DataFrame, handling: str) -> pd.DataFrame:
    errors = (candles['High'] < candles['Low']) | \
             ~(candles['Low'] <= candles['Open']) | \
             ~(candles['Open'] <= candles['High']) | \
             ~(candles['Low'] <= candles['Close']) | \
             ~(candles['Close'] <= candles['High'])

    for index in candles[errors].index:
        if index not in (0, len(candles) - 1) and handling == 'Adapt':
            candles.loc[index, 'Open'] = candles.loc[index - 1, 'Close']
            candles.loc[index, 'High'] = max(candles.loc[index - 1, 'Close'], candles.loc[index + 1, 'Open'])
            candles.loc[index, 'Close'] = candles.loc[index + 1, 'Open']
            candles.loc[index, 'Low'] = min(candles.loc[index - 1, 'Close'], candles.loc[index + 1, 'Open'])
        else:
            candles = candles.drop(index).reset_index(drop=True)

    return candles

def getCandleDirection(candles: pd.DataFrame) -> pd.DataFrame:
    conditions = [
        (candles['Close'] > candles['Open']),
        (candles['Close'] < candles['Open'])
    ]

    choices = ['Bullish', 'Bearish']

    candles['Direction'] = np.select(conditions, choices, default='Doji')

    return candles

def getGlobalAverage(candles: pd.DataFrame) -> pd.DataFrame:
    candles['Global Average'] = (candles['High'] + candles['Low']) / 2

    return candles

def getLocalAverage(candles: pd.DataFrame) -> pd.DataFrame:
    candles['Local Average'] = (candles['Open'] + candles['Close']) / 2

    return candles

def getnTimesAverage(candles: pd.DataFrame, n: int, type: str) -> pd.DataFrame:
    candles[f'{n} Times {type} Average'] = candles[f'{type} Average'].rolling(n).mean()

    return candles