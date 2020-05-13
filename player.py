class Player:
    
    def __init__(self, symbol, num):
        self.id = num
        self.symbol = symbol
        
    def getSymbol(self):
        return self.symbol
    
    def getID(self):
        return self.id