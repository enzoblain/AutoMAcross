class Candle():
    def __init__(self, timestamp, openPrice, closePrice, maxPrice, minPrice):
        self.timestamp = timestamp
        self.open = openPrice
        self.close = closePrice
        self.max = maxPrice
        self.min = minPrice
        self.direction = self.getDirection()
        self.error = self.getSyntaxError()
    
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

    def getSyntaxError(self):
        if self.max < self.min:
            return True
        
        if self.direction == "Bullish":
            return not (self.close < self.max and self.open > self.min)
        elif self.direction == "Bearish":
            return not (self.close > self.min and self.open < self.max)
        
        return False