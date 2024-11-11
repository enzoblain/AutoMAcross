from Scripts.checker import config_checker
from Scripts.functions import getFromEnv

def setup():
    config = config_checker()
    config['Api']['Key'] = getFromEnv('API_KEY')

    return config