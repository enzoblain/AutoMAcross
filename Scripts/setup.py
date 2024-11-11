from Scripts.checker import config_checker
from Scripts.functions import getFromEnv
from Scripts.data_handler import getForexData

def setup():
    config = config_checker()
    config['Api']['Key'] = getFromEnv('API_KEY')

    data = getForexData(config['Api']['Url'], config['Api']['Key'], 'EUR/USD', interval='5min')

    print(data)

    return config, data