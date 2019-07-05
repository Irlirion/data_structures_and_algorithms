class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        lst = '['
        node = self.head
        while node.next is not None:
            lst += str(node) + ', '
            node = node.next
        return lst + str(node) + ']'

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        lst = []
        node = self.head
        while node is not None:
            if node.value == val:
                lst.append(node)
            node = node.next
        return lst

    def delete(self, val, all=False):
        if self.head is None:
            return

        if all:
            for node in self.find_all(val):
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
        else:
            node = self.find(val)
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

    def clean(self):
        pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код

    def add_in_head(self, newNode):
        pass  # здесь будет ваш код
