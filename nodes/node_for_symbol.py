from dataclasses import dataclass


@dataclass
class NodeForSymbol:
    symbol: bytes
    freq: int
    bit0 = None
    bit1 = None

    def __lt__(self, other):
        return self.freq < other.freq
        