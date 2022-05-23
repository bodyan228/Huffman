class NodeForSymbol:
    symbol: bytes
    freq: int
    bit0: None
    bit1: None
    
    def __init__(self, s, fr):
        self.symbol = s
        self.freq = fr
        self.bit0 = None
        self.bit1 = None
    
    def __str__(self):
        return f'symbol:{self.symbol} freq:{self.freq}'
    