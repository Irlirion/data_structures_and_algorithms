class HashSet:
    def __init__(self, *args):
        self.__items = [None] * 10
        self.__num_items = 0
        for item in args:
            self.add(item)

    @staticmethod
    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] is not None:
            if items[idx] == item:
                # item already in set
                return False
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
            idx = (idx + 1) % len(items)
        if loc < 0:
            loc = idx
        items[loc] = item
        return True

    @staticmethod
    def __rehash(old_list, new_list):
        for x in old_list:
            if x is not None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, new_list)
        return new_list

    def add(self, item):
        if HashSet.__add(item, self.__items):
            self.__num_items += 1
            load = self.__num_items / len(self.__items)
            if load >= 0.75:
                self.__items = HashSet.__rehash(self.__items,
                                                [None] * 2 * len(self.__items))

    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    @staticmethod
    def __remove(item, items):
        idx = hash(item) % len(items)
        while items[idx] is not None:
            if items[idx] == item:
                next_idx = (idx + 1) % len(items)
                if items[next_idx] is None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            idx = (idx + 1) % len(items)
        return False

    def remove(self, item):
        if HashSet.__remove(item, self.__items):
            self.__num_items -= 1
            load = max(self.__num_items, 10) / len(self.__items)
            if load <= 0.25:
                self.__items = HashSet.__rehash(self.__items, [None] * int(
                    len(self.__items) / 2))
        else:
            raise KeyError('Item not in HashSet')

    def __contains__(self, item):
        idx = hash(item) % len(self.__items)
        while self.__items[idx] is not None:
            if self.__items[idx] == item:
                return True
            idx = (idx + 1) % len(self.__items)
        return False

    def __iter__(self):
        for i in range(len(self.__items)):
            if self.__items[i] is not None and type(
                    self.__items[i]) != HashSet.__Placeholder:
                yield self.__items[i]

    def __getitem__(self, item):
        idx = hash(item) % len(self.__items)
        while self.__items[idx] is not None:
            if self.__items[idx] == item:
                return self.__items[idx]
            idx = (idx + 1) % len(self.__items)
        return None

    def __len__(self):
        return self.__num_items


if __name__ == '__main__':
    h_set = HashSet(*range(100))
    print(len(h_set))
    h_set.remove(10)
    for item in h_set:
        if item in h_set:
            print(h_set[item])
            h_set.add(item + 100)
    for i in range(100):
        h_set.add(i)
    try:
        h_set.remove(-1)
    except KeyError:
        print("OK")
    h_set1 = HashSet()
    h_set1.add(2)
    h_set1.add(3)
    print(h_set1[3])
