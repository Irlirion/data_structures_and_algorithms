class PowerSet:

    def __init__(self):
        self.size = 20000
        self.step = 5
        self.slots = [None] * self.size
        self.ln = 0

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

    def find(self, value):
        i = self.hash_fun(value)
        if value == self.slots[i]:
            return i
        else:
            for i in range(self.size):
                if self.slots[i] == value:
                    return i
            return None

    def size(self):
        return self.ln

    def put(self, value):
        if not self.get(value):
            i = self.seek_slot(value)
            if i is not None:
                self.slots[i] = value
                self.ln += 1
            return i

    def get(self, value):
        if self.slots[self.hash_fun(value)] is not None or value in self.slots:
            return True
        return False

    def remove(self, value):
        i = self.find(value)
        if i is not None:
            self.slots[i] = None
            self.ln -= 1
            return True
        return False

    def intersection(self, set2):
        new_set = PowerSet()
        for el in self.slots:
            if el is None:
                continue
            if set2.get(el):
                new_set.put(el)
        return new_set

    def union(self, set2):
        new_set = PowerSet()
        for el in self.slots:
            if el is None:
                continue
            new_set.put(el)
        for el in set2.slots:
            if el is None:
                continue
            if not new_set.get(el):
                new_set.put(el)
        return new_set

    def difference(self, set2):
        new_set = PowerSet()
        for el in self.slots:
            if el is None:
                continue
            if not set2.get(el):
                new_set.put(el)
        return new_set

    def issubset(self, set2):
        flag = True
        for el in set2.slots:
            if el is None:
                continue
            if not self.get(el):
                flag = False
        return flag
