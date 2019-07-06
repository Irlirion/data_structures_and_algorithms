class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size():
            val = self.deque[0]
            self.deque = self.deque[1:]
            return val
        return None

    def removeTail(self):
        if self.size():
            return self.deque.pop()
        return None

    def size(self):
        return len(self.deque)
