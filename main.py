from Components.candle import Candle

from datetime import datetime

candles = [
    Candle(timestamp=datetime(2024, 11, 8, 10, 0, 0), openPrice=100, closePrice=105, maxPrice=110, minPrice=95),
    Candle(timestamp=datetime(2024, 11, 8, 10, 5, 0), openPrice=105, closePrice=100, maxPrice=110, minPrice=95),
    Candle(timestamp=datetime(2024, 11, 8, 10, 10, 0), openPrice=100, closePrice=100, maxPrice=110, minPrice=95),
    Candle(timestamp=datetime(2024, 11, 8, 10, 15, 0), openPrice=95, closePrice=105, maxPrice=90, minPrice=100),
    Candle(timestamp=datetime(2024, 11, 8, 10, 20, 0), openPrice=100, closePrice=110, maxPrice=105, minPrice=95),
    Candle(timestamp=datetime(2024, 11, 8, 10, 25, 0), openPrice=110, closePrice=90, maxPrice=95, minPrice=100),
    Candle(timestamp=datetime(2024, 11, 8, 10, 30, 0), openPrice=100, closePrice=105, maxPrice=110, minPrice=95),
    Candle(timestamp=datetime(2024, 11, 8, 10, 35, 0), openPrice=105, closePrice=95, maxPrice=100, minPrice=90),
    Candle(timestamp=datetime(2024, 11, 8, 10, 40, 0), openPrice=100, closePrice=100, maxPrice=90, minPrice=100),
    Candle(timestamp=datetime(2024, 11, 8, 10, 45, 0), openPrice=110, closePrice=120, maxPrice=115, minPrice=105)
]

for candle in candles:
    if candle.error:
        print(f"Warning : The provided candle ({candle.timestamp}) has not correct data")