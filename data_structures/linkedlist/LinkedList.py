class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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
        return lst  # здесь будет ваш код

    def delete(self, val, all=False):
        if self.head is None:
            return

        node_before = None
        node = self.head
        while node is not None:
            if node.value == val:
                if node_before is None:
                    self.head = self.head.next
                elif node.next is None:
                    node_before.next = None
                    self.tail = node_before
                else:
                    node_before.next = node.next

                if all:
                    node = node.next
                else:
                    return
            else:
                node_before = node
                node = node.next

    def clean(self):
        pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код
