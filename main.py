from Scripts.setup import setup
from Scripts.data_handler import dataVisualizer


if __name__ == '__main__':
    config, data = setup()

    print(data)

    dataSample = data.head(100)

    