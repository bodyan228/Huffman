from dataclasses import dataclass


@dataclass
class NodeForBit:
    bit0: int
    bit1: int
    freq: int
    
    def __lt__(self, other):
        return self.freq < other.freq
    