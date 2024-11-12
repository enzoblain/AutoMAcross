from Scripts.setup import setup
from Algorithms.MACross import alertCrossed, MACrossInAction
from Components.candle import getnTimesAverage
from Scripts.data_handler import dataVisualizer
import pandas as pd


if __name__ == '__main__':
    config, data = setup()

    a1 = [1, 2, 3, 4, 5, 10, 20, 25, 50, 100]
    a2 = [2, 3, 4, 5, 10, 20, 25, 50, 100]
    types = ['Global', 'Local']

    solds = []

    for k in a1:
        for type in types:
            data = getnTimesAverage(data, k, type)

    for i in a1:
        for j in a2:
            for type in types:
                if i < j:
                    alerts = alertCrossed(data, i, j, type)
                    sold = MACrossInAction(data, alerts, type)
                    solds.append([i, j, sold, type])

    solds_df = pd.DataFrame(solds, columns=['i', 'j', 'sold', 'type'])

    solds_df = solds_df.sort_values(by='sold', ascending=False)

    print(solds_df)