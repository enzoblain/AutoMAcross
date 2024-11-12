from Scripts.setup import setup
from Algorithms.MACross import alertCrossed, MACrossInAction
from Components.candle import getnTimesAverage

import time
import pandas as pd


if __name__ == '__main__':
    solds = []

    time_window = 5000

    config, data = setup(time_window)

    data = getnTimesAverage(data, config['Average 1'], config['Average type'])
    data = getnTimesAverage(data, config['Average 2'], config['Average type'])

    alerts = alertCrossed(data, config['Average 1'], config['Average 2'], config['Average type'])
    sold = MACrossInAction(data, alerts, config['Average type'], config['Balance'])

    print(sold)