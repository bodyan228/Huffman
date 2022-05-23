from collections import defaultdict, deque


class PriorityQueue:
    """Очередь вида [[priority,(code symbol,number of occurrences)]"""
    size: int
    storage: defaultdict
    
    def __init__(self):
        self.storage = defaultdict(list)
        self.size = 0
        
    def size(self):
        return self.size
    
    def enqueue(self, priority, item):
        if priority not in self.storage.keys():
            self.storage[priority] = deque()
        self.storage[priority].append(item)
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise Exception('Queue is empty')
        sorted_list = sorted(self.storage.items())
        self.size -= 1
        for q in sorted_list:
            if len(q[1]) > 0:
                return q[1].popleft()
        
        raise Exception('Queue error')
        
        