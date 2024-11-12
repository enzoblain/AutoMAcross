from typing import List, Tuple
import pandas as pd

def alertCrossed(candles: pd.DataFrame, n1: int, n2: int, type: str) -> List[List[Tuple[int, str]]]:
    alerts = []

    for index in range(1, len(candles)):
        if candles.loc[index - 1, f'{n1} Times {type} Average'] < candles.loc[index - 1, f'{n2} Times {type} Average'] and \
           candles.loc[index, f'{n1} Times {type} Average'] > candles.loc[index, f'{n2} Times {type} Average']:
            alerts.append([index, 'Crossed Up'])
        elif candles.loc[index - 1, f'{n1} Times {type} Average'] > candles.loc[index - 1, f'{n2} Times {type} Average'] and \
             candles.loc[index, f'{n1} Times {type} Average'] < candles.loc[index, f'{n2} Times {type} Average']:
            alerts.append([index, 'Crossed Down'])

    return alerts

def MACrossInAction(candles: pd.DataFrame, alerts: List[List[Tuple[int, str]]], type: str, balance: int) -> int:
    holdings = 0
    sold = 0

    if alerts[0][1] == 'Crossed Up':
        price = candles.loc[alerts[0][0], f'{type} Average']
        holdings = balance / price
        balance = 0
    else:
        price = candles.loc[alerts[0][0], f'{type} Average']
        if holdings > 0:
            sold = holdings * price
            balance += sold
            holdings = 0

    i = 1
    while i < len(alerts) - 1:
        price = candles.loc[alerts[i][0], f'{type} Average']
        if alerts[i][1] == 'Crossed Up':
            if balance > 0:
                holdings = balance / price
                balance = 0
        elif alerts[i][1] == 'Crossed Down':
            if holdings > 0:
                sold = holdings * price
                balance += sold
                holdings = 0
        i += 1

    if alerts[-1][1] == 'Crossed Down' and holdings > 0:
        price = candles.loc[alerts[-1][0], f'{type} Average']
        sold = holdings * price
        balance += sold
        holdings = 0

    return balance