from Scripts.checker import config_checker
from Scripts.functions import getFromEnv
from Scripts.data_handler import getForexData
from Components.candle import filterCandles, getGlobalAverage, getLocalAverage

from typing import Dict, Tuple
import pandas as pd

def setup(candleNumber: int) -> Tuple[Dict, pd.DataFrame]:
    config = config_checker()
    config['Api']['Key'] = getFromEnv('API_KEY')

    data = getForexData(config['Api']['Url'], config['Api']['Key'], config['Symbol'], interval=config['Time range'], timeZone=config['Time zone'], outputSize=candleNumber)

    if config['Average type'] == 'Global':
        data = getGlobalAverage(filterCandles(data, config['Error handling']))
    else:
        data = getLocalAverage(filterCandles(data, config['Error handling']))

    return config, data