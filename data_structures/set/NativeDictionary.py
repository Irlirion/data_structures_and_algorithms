class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return hash(key) % self.size

    def is_key(self, key):
        i = self.hash_fun(key)
        if self.slots[i] == key:
            return True
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        i = self.hash_fun(key)
        if self.slots[i] == key:
            return
        if self.slots[i] is None:
            self.slots[i] = key
            self.values[i] = value
        else:
            for i in range(self.size):
                if self.slots[i] is None:
                    self.slots[i] = key
                    self.values[i] = value
                    return

    def get(self, key):
        i = self.hash_fun(key)
        if self.slots[i] == key:
            return self.values[i]
        return self.values[self.slots.index(key)] if key in self.slots else None
