from Scripts.checker import config_checker
from Scripts.functions import getFromEnv
from Scripts.data_handler import getForexData
from Components.candle import filterCandles, getCandleDirection

from typing import Dict, Tuple
import pandas as pd

def setup() -> Tuple[Dict, pd.DataFrame]:
    config = config_checker()
    config['Api']['Key'] = getFromEnv('API_KEY')

    data = getForexData(config['Api']['Url'], config['Api']['Key'], 'EUR/USD', interval='5min')

    data = getCandleDirection(filterCandles(data, config['Error handling']))

    return config, data