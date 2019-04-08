from HashSet import HashSet


class HashMap:
    class __KVPair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.key == other.key

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def __hash__(self):
            return hash(self.key)

    def __init__(self):
        self.h_set = HashSet()

    def __len__(self):
        return len(self.h_set)

    def __contains__(self, item):
        return self.__KVPair(item, None) in self.h_set

    def __setitem__(self, key, value):
        self.h_set.add(self.__KVPair(key, value))

    def __getitem__(self, key):
        if self.__KVPair(key, None) in self.h_set:
            val = self.h_set[self.__KVPair(key, None)].get_value()
            return val
        raise KeyError("Key " + str(key) + " not in HashMap")

    def __iter__(self):
        for x in self.h_set:
            yield x.get_value()


if __name__ == '__main__':
    h_map = HashMap()

    h_map[0] = 0
    print(h_map[0])

    try:
        print(h_map[1])
    except KeyError:
        print("OK")

    for i in range(10):
        h_map[i] = i
    print(0 in h_map)
    print(len(h_map))
    for el in h_map:
        print(el)
    print(h_map[0] == h_map[1])
    h_map[11] = '1'
    print(h_map[1] == h_map[11])
