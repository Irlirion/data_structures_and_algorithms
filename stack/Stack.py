class Stack:
    def __init__(self):
        self.__items = []

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Attempt to pop an empty stack')
        top_idx = len(self.__items) - 1
        item = self.__items[top_idx]
        del self.__items[top_idx]
        return item

    def push(self, item):
        self.__items.append(item)

    def top(self):
        if self.is_empty():
            raise RuntimeError('Attempt to get top of empty stack')
        top_idx = len(self.__items) - 1
        return self.__items[top_idx]

    def is_empty(self):
        return len(self.__items) == 0


if __name__ == '__main__':
    s = Stack()
    lst = list(range(10 ** 5))
    lst2 = []

    for k in lst:
        s.push(k)

    if s.top() == 10 ** 5 - 1:
        print('Test 1 Passed')
    while not s.is_empty():
        lst2.append(s.pop())

    lst2.reverse()

    if lst2 == lst:
        print('Test 2 Passed')

    try:
        s.pop()
    except RuntimeError:
        print('Test 3 Passed')

    try:
        s.top()
    except RuntimeError:
        print('Test 4 Passed')
