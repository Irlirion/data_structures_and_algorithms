class PowerSet:

    def __init__(self):
        self.slots = dict()

    def size(self):
        return len(self.slots)

    def put(self, value):
        s = str(value)
        if s not in self.slots:
            self.slots[s] = value

    def get(self, value):
        return str(value) in self.slots

    def remove(self, value):
        if self.get(value):
            self.slots.pop(str(value))
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
