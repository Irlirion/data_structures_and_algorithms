class LinkedList:
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_item(self, item):
            self.item = item

        def set_next(self, next):
            self.next = next

    def __init__(self, *args):
        self.__first = LinkedList.__Node(None, None)
        self.__last = self.__first
        self.__num_items = 0
        for element in args:
            self.append(element)

    def __getitem__(self, index):
        if 0 <= index < self.__num_items:
            cursor = self.__first.get_next()
            for _ in range(index):
                cursor = cursor.get_next()
            return cursor.get_item()
        raise IndexError('LinkedList assignment index out of range')

    def __setitem__(self, index, item):
        if 0 <= index < self.__num_items:
            cursor = self.__first.get_next()
            for _ in range(index):
                cursor = cursor.get_next()
            cursor.set_item(item)
            return
        raise IndexError('LinkedList assignment index out of range')

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                'Concatenate undefined for ' + str(type(self)) + ' + ' + str(
                    type(other)))
        result = LinkedList()
        cursor = self.__first.get_next()
        while cursor:
            result.append(cursor.get_item())
            cursor = cursor.get_next()
        cursor = other.__first.get_next()
        while cursor:
            result.append(cursor.get_item())
            cursor = cursor.get_next()
        return result

    def __str__(self):
        if self.__num_items > 0:
            out = '['
            cursor = self.__first.get_next()
            while cursor.get_next():
                out += str(cursor.get_item()) + ', '
                cursor = cursor.get_next()
            return out + str(cursor.get_item()) + ']'
        return '[]'

    def __len__(self):
        return self.__num_items

    def append(self, item):
        node = LinkedList.__Node(item)
        self.__last.set_next(node)
        self.__last = node
        self.__num_items += 1

    def insert(self, index, item):
        cursor = self.__first
        if index < self.__num_items:
            for _ in range(index):
                cursor = cursor.get_next()
            node = LinkedList.__Node(item, cursor.get_next())
            cursor.set_next(node)
            self.__num_items += 1
        else:
            self.append(item)


if __name__ == '__main__':
    l_list = LinkedList(1, 0, 3)
    l_list.append(1)
    l_list.insert(2, 1)
    l_list.insert(100, 100)
    print(len(l_list))
    print(l_list)
    print(LinkedList())
    l_list += LinkedList(1, 3)
    try:
        l_list += 2
    except TypeError:
        print('TypeError')
    l_list[1] = 2
    try:
        l_list[100] = 2
    except IndexError:
        print('IndexError')
    print(l_list[1])
    try:
        print(l_list[100])
    except IndexError:
        print('IndexError')
