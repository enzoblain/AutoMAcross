import json
import os
import requests
import time
import datetime
import pytz

import pandas as pd

from dotenv import load_dotenv

def getFromEnv(attr: str) -> str:
    load_dotenv()

    value = os.getenv(attr)

    if not value:
        raise ValueError(f"{attr} not found. Please set it in the .env file.")

    return value

def getConfig() -> dict:
    config_path = 'config.json'
    with open(config_path, 'r') as file:
        config = json.load(file)

    config['Api']['Key'] = getFromEnv('API_KEY')

    return config

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

def getGlobalAverage(candles: pd.DataFrame) -> pd.DataFrame:
    candles['Global Average'] = (candles['High'] + candles['Low']) / 2

    return candles

def getLocalAverage(candles: pd.DataFrame) -> pd.DataFrame:
    candles['Local Average'] = (candles['Open'] + candles['Close']) / 2

    return candles

def getnTimesAverage(data: pd.DataFrame, average: int, averageType: str) -> pd.DataFrame:
    data[f'{average} Times {averageType} Average'] = data[f'{averageType} Average'].rolling(average).mean()

    return data

def getAveragePosition(data, averageType, average1, average2):
    data['Average position'] = data.apply(lambda row: "Up" if row[f'{average1} Times {averageType} Average'] > row[f'{average2} Times {averageType} Average'] else "Down", axis=1)

    return data

def getBuyorSellIndication(data):
    data['Previous position'] = data['Average position'].shift(1)

    def buy_or_sell(row):
        if row['Average position'] == "Up" and row['Previous position'] == "Down":
            return "Buy"
        elif row['Average position'] == "Down" and row['Previous position'] == "Up":
            return "Sell"
        else:
            return None

    data['Buy or Sell'] = data.apply(buy_or_sell, axis=1)

    data = data.drop(columns=['Previous position'])

    return data

def main():
    config = getConfig()

    data = getForexData(config['Api']['Url'], config['Api']['Key'], config['Symbol'], config['Time range'], config['Time zone'], 5)

    if config['Average type'] == 'Global':
        data = getGlobalAverage(filterCandles(data, config['Error handling']))
    else:
        data = getLocalAverage(filterCandles(data, config['Error handling']))

    data = getnTimesAverage(data, config['Average 1'], config['Average type'])
    data = getnTimesAverage(data, config['Average 2'], config['Average type'])
    data = getAveragePosition(data, config['Average type'], config['Average 1'], config['Average 2'])
    data = getBuyorSellIndication(data)

    return {
        "Buy or Sell" : data.loc[len(data) - 2]['Buy or Sell'],
        "Price": data.loc[len(data) - 1]['Open']
    }

if __name__ == "__main__":
    balance, holdings = 100, 0
    print(f"Initial Balance: {balance}")
    while True:
        now = datetime.datetime.now(pytz.timezone('Europe/Paris'))

        startTime = datetime.time(8, 30)
        endTime = datetime.time(20, 30)

        if startTime <= now.time() <= endTime:
            todo = main()
            print(todo)

            if todo['Buy or Sell']:
                printBalance = False
                if todo['Buy or Sell'] == 'Buy':
                    printBalance = True
                    print(f"Buying at {todo['Price']}")
                    holdings = balance / todo['Price']
                    balance = 0
                elif todo['Buy or Sell'] == 'Sell' and holdings != 0:
                    printBalance = True
                    print(f"Selling at {todo['Price']}")
                    balance = holdings * todo['Price']
                    holdings = 0

                if printBalance:
                    print(f"Updated Balance: {balance}")   
                if holdings != 0:
                    print(f"Updated Holdings Price: {holdings * todo['Price']}")
            time.sleep(60) # in case of 1 minute interval because 60 is not enough to do it in 1 minute