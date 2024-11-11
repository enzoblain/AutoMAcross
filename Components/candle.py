from datetime import datetime

class Candle():
    def __init__(self, timestamp, openPrice, closePrice, maxPrice, minPrice):
        self.timestamp = timestamp
        self.open = openPrice
        self.close = closePrice
        self.max = maxPrice
        self.min = minPrice
        self.error = self.getDataError() or not self.getValidDataTypes()
        self.direction = self.getDirection() if not self.error else None
    
    def __str__(self):
        return (f"Candle(Open: {self.open}, Close: {self.close}, "
                f"Max: {self.max}, Min: {self.min}, "
                f"Direction: {self.direction}, Error: {self.error})")
    
    def getDirection(self):
        if self.close > self.open:
            return "Bullish"
        elif self.close < self.open:
            return "Bearish"
        else:
            return "Doji"

    def getDataError(self):
        if self.max < self.min:
            return True
        
        if not (self.min <= self.open <= self.max and self.min <= self.close <= self.max):
            return True
        
        return False

    def getValidDataTypes(self):
        if not isinstance(self.timestamp, datetime):
            return False
        if not isinstance(self.open, (int, float)):
            return False
        if not isinstance(self.close, (int, float)):
            return False
        if not isinstance(self.max, (int, float)):
            return False
        if not isinstance(self.min, (int, float)):
            return False
        return True