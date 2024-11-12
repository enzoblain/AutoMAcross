from Scripts.checker import config_checker
from Scripts.functions import getFromEnv
from Scripts.data_handler import getForexData
from Components.candle import filterCandles, getCandleDirection, getGlobalAverage, getLocalAverage

from typing import Dict, Tuple
import pandas as pd

def setup(interval: str) -> Tuple[Dict, pd.DataFrame]:
    config = config_checker()
    config['Api']['Key'] = getFromEnv('API_KEY')

    data = getForexData(config['Api']['Url'], config['Api']['Key'], 'EUR/USD', interval=interval, timeZone=config['Time zone'])

    data = getCandleDirection(filterCandles(data, config['Error handling']))
    data = getGlobalAverage(data)
    data = getLocalAverage(data)

    return config, data