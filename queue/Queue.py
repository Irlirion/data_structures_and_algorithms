class Queue:
    def __init__(self):
        self.__items = []
        self.__front_idx = 0

    def __compress(self):
        new_list = []
        for i in range(self.__front_idx, len(self.__items)):
            new_list.append(self.__items[i])
        self.__items = new_list
        self.__front_idx = 0

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Attempt to dequeue an empty queue')
        if self.__front_idx * 2 > len(self.__items):
            self.__compress()
        item = self.__items[self.__front_idx]
        self.__front_idx += 1
        return item

    def enqueue(self, item):
        self.__items.append(item)

    def front(self):
        if self.is_empty():
            raise RuntimeError('Attempt to access front of empty queue')
        return self.__items[self.__front_idx]

    def is_empty(self):
        return self.__front_idx == len(self.__items)


if __name__ == '__main__':
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k)

    if q.front() == 0:
        print('Test 1 Passed')

    while not q.is_empty():
        lst2.append(q.dequeue())

    if lst2 == lst:
        print('Test 2 Passed')

    for k in lst:
        q.enqueue(k)

    lst2 = []

    while not q.is_empty():
        lst2.append(q.dequeue())

    if lst2 == lst:
        print('Test 3 Passed')

    try:
        q.dequeue()
    except RuntimeError:
        print('Test 4 Passed')

    try:
        q.front()
    except RuntimeError:
        print('Test 5 Passed')
