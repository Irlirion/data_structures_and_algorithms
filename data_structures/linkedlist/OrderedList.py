class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    # def __str__(self):
    #     return str(self.value)


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value < v2.value:
            return -1
        elif v1.value > v2.value:
            return 1
        return 0

    # def __str__(self):
    #     r = '['
    #     node = self.head
    #     while node.next is not None:
    #         r += str(node.value) + ', '
    #         node = node.next
    #     return r + str(node.value) + ']'

    def add(self, value):
        new_node = Node(value)
        if self.head == self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node is not None:
            if self.__ascending and self.compare(new_node, node) <= 0 or not self.__ascending and self.compare(
                    new_node, node) >= 0:
                if node.prev is None:
                    # Голова
                    new_node.next = node
                    node.prev = new_node
                    self.head = new_node
                else:
                    # Между
                    node.prev.next = new_node
                    new_node.prev = node.prev
                    new_node.next = node
                    node.prev = new_node
                return
            elif node.next is None:
                # Хвост
                node.next = new_node
                new_node.prev = node
                self.tail = new_node
                return
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        if self.head is None:
            return

        node = self.find(val)
        if node is not None:
            if node.prev is None:
                self.head = node.next
                if self.head is None:
                    self.tail = None
                else:
                    node.next.prev = None
            elif node.next is None:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        pass  # здесь будет ваш код

    def len(self):
        node = self.head
        ln = 0
        while node is not None:
            ln += 1
            node = node.next
        return ln

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            # r.append(node.value)
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def compare(self, v1, v2):
        if v1.value.strip() < v2.value.strip():
            return -1
        elif v1.value.strip() > v2.value.strip():
            return 1
        return 0
