class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None



class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

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
        while self.head is not None:
            node = self.head
            self.head = node.next
            node.next = None
            node.prev = None
            del node
        self.tail = None

    def len(self):
        len = 0
        node = self.head
        while node is not None:
            len += 1
            node = node.next
        return len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            node = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
            newNode.next = node
            if node is None:
                self.tail = newNode
            else:
                node.prev = newNode

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
