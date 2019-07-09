# from data_structures.set.HashTable import HashTable
#
#
class PowerSet(HashTable):

    def __init__(self):
        super().__init__(20000, 3)
        self.ln = 0

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
