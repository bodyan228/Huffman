from nodes.node import Node


class NodeForBit:
    freq: int
    bit0: Node
    bit1: Node
    
    def __init__(self, b0, b1, fr):
        self.bit0 = b0
        self.bit1 = b1
        self.freq = fr
        
    def __str__(self):
        return f'bit0: {self.bit0}, bit1: {self.bit1}, freq = {self.freq}'
        