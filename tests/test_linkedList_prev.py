from unittest import TestCase
from data_structures.linkedlist.LinkedList import LinkedList, Node


def values(lst):
    vals = []
    node = lst.head
    while node is not None:
        vals.append(node.value)
        node = node.next
    return vals


class TestLinkedList(TestCase):
    def test_delete(self):
        lst = LinkedList()
        lst.delete(1)
        self.assertEqual(values(lst), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        lst.add_in_tail(Node(2))
        lst.delete(2)
        self.assertEqual(values(lst), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        nd = Node(2)
        nd1 = Node(1)
        lst.add_in_tail(nd)
        lst.add_in_tail(nd1)
        lst.delete(1)
        self.assertEqual(values(lst), [2])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd)

        lst.add_in_tail(nd1)
        lst.delete(2)
        self.assertEqual(values(lst), [1])
        self.assertEqual(lst.head, nd1)
        self.assertEqual(lst.tail, nd1)

        lst = LinkedList()
        nd2 = Node(3)
        lst.add_in_tail(nd1)
        lst.add_in_tail(nd)
        lst.add_in_tail(nd2)
        lst.delete(2)
        self.assertEqual(values(lst), [1, 3])
        self.assertEqual(lst.head, nd1)
        self.assertEqual(lst.tail, nd2)

        lst = LinkedList()
        nd3 = Node(3)
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(nd2)
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(nd3)
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.delete(1, all=True)

        self.assertEqual(values(lst), [3, 3])
        self.assertEqual(lst.head, nd2)
        self.assertEqual(lst.tail, nd3)

    def test_find_all(self):
        lst = LinkedList()
        self.assertEqual(lst.find_all(1), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        nd = Node(2)
        lst.add_in_tail(nd)
        self.assertEqual(lst.find_all(2), [nd])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd)

        nd1 = Node(1)
        nd2 = Node(1)
        nd3 = Node(1)
        lst.add_in_tail(nd1)
        lst.add_in_tail(nd2)
        lst.add_in_tail(Node(3))
        lst.add_in_tail(nd3)
        self.assertEqual(lst.find_all(1), [nd1, nd2, nd3])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd3)

    def test_clean(self):
        lst = LinkedList()
        lst.clean()
        self.assertEqual(values(lst), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        lst.add_in_tail(Node(1))
        lst.clean()
        self.assertEqual(values(lst), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(2))
        lst.add_in_tail(Node(3))
        lst.clean()
        self.assertEqual(values(lst), [])
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

    def test_len(self):
        lst = LinkedList()
        self.assertEqual(lst.len(), 0)
        self.assertEqual(lst.head, None)
        self.assertEqual(lst.tail, None)

        nd = Node(1)
        lst.add_in_tail(nd)
        self.assertEqual(lst.len(), 1)
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd)

        nd1 = Node(1)
        lst.add_in_tail(nd1)
        self.assertEqual(lst.len(), 2)
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd1)

        lst.delete(1)
        self.assertEqual(lst.len(), 1)
        self.assertEqual(lst.head, nd1)
        self.assertEqual(lst.tail, nd1)

    def test_insert(self):
        lst = LinkedList()
        nd = Node(1)
        lst.insert(None, nd)
        self.assertEqual(values(lst), [1])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd)

        nd1 = Node(2)
        lst.insert(nd, nd1)
        self.assertEqual(values(lst), [1, 2])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd1)

        nd2 = Node(3)
        lst.insert(nd, nd2)
        self.assertEqual(values(lst), [1, 3, 2])
        self.assertEqual(lst.head, nd)
        self.assertEqual(lst.tail, nd1)

        nd3 = Node(4)
        lst.insert(None, nd3)
        self.assertEqual(values(lst), [4, 1, 3, 2])
        self.assertEqual(lst.head, nd3)
        self.assertEqual(lst.tail, nd1)
