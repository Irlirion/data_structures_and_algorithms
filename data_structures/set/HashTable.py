class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return hash(value) % self.size

    def seek_slot(self, value):
        i = self.hash_fun(value)
        while i < self.size and self.slots[i] is not None:
            i += self.step
        if i >= self.size:
            i = 0
            while i < self.size and self.slots[i] is not None:
                i += 1
        if i >= self.size:
            return None
        return i

    def put(self, value):
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
        return i

    def find(self, value):
        i = self.hash_fun(value)
        if value == self.slots[i]:
            return i
        else:
            for i in range(self.size):
                if self.slots[i] == value:
                    return i
            return None
