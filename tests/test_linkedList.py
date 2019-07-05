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

        lst.add_in_tail(Node(2))
        lst.delete(2)
        self.assertEqual(values(lst), [])

        lst.add_in_tail(Node(2))
        lst.add_in_tail(Node(1))
        lst.delete(1)
        self.assertEqual(values(lst), [2])

        lst.add_in_tail(Node(1))
        lst.delete(2)
        self.assertEqual(values(lst), [1])

        lst = LinkedList()
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(2))
        lst.add_in_tail(Node(3))
        lst.delete(2)
        self.assertEqual(values(lst), [1, 3])

        lst = LinkedList()
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(3))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(3))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(1))
        lst.delete(1, all=True)

        self.assertEqual(values(lst), [3, 3])

    def test_find_all(self):
        lst = LinkedList()
        self.assertEqual(lst.find_all(1), [])

        nd = Node(2)
        lst.add_in_tail(nd)
        self.assertEqual(lst.find_all(2), [nd])

        nd1 = Node(1)
        nd2 = Node(1)
        nd3 = Node(1)
        lst.add_in_tail(nd1)
        lst.add_in_tail(nd2)
        lst.add_in_tail(Node(3))
        lst.add_in_tail(nd3)
        self.assertEqual(lst.find_all(1), [nd1, nd2, nd3])

    def test_clean(self):
        lst = LinkedList()
        lst.clean()
        self.assertEqual(values(lst), [])

        lst.add_in_tail(Node(1))
        lst.clean()
        self.assertEqual(values(lst), [])

        lst.add_in_tail(Node(1))
        lst.add_in_tail(Node(2))
        lst.add_in_tail(Node(3))
        lst.clean()
        self.assertEqual(values(lst), [])

    def test_len(self):
        lst = LinkedList()
        self.assertEqual(lst.len(), 0)

        lst.add_in_tail(Node(1))
        self.assertEqual(lst.len(), 1)

        lst.add_in_tail(Node(1))
        self.assertEqual(lst.len(), 2)

        lst.delete(1)
        self.assertEqual(lst.len(), 1)
