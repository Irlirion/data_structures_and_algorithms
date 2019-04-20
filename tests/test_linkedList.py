from unittest import TestCase
from data_structures.linkedlist.LinkedList import LinkedList


class TestLinkedList(TestCase):
    def test_append(self):
        lst = LinkedList()
        lst.append(1)
        self.assertEqual(str(lst), '[1]')

    def test_insert(self):
        lst = LinkedList(1, 2, 4)
        lst.insert(2, 3)
        self.assertEqual(str(lst), '[1, 2, 3, 4]')
