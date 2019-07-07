from unittest import TestCase
from data_structures.linkedlist.OrderedList import OrderedList, OrderedStringList, Node


class TestOrderedList(TestCase):
    def setUp(self):
        self.ol_up = OrderedList(True)
        self.ol_dwn = OrderedList(False)
        self.nd0 = Node(0)
        self.nd1 = Node(1)

    def test_compare(self):
        self.assertEqual(self.ol_up.compare(self.nd0, self.nd1), -1)
        self.assertEqual(self.ol_up.compare(self.nd1, self.nd0), 1)
        self.assertEqual(self.ol_up.compare(self.nd0, self.nd0), 0)

    def test_add(self):
        # Тестирование восходящего списка
        self.ol_up.add(0)
        self.assertEqual(self.ol_up.head.value, 0)
        self.assertEqual(self.ol_up.tail.value, 0)
        self.assertEqual(self.ol_up.get_all(), [0], 'Ошибка во время вставки в пустой список')
        self.ol_up.add(1)
        self.assertEqual(self.ol_up.get_all(), [0, 1],
                         'Ошибка во время вставки в восходящий список из 1 элемента вверх')
        self.assertEqual(self.ol_up.head.value, 0)
        self.assertEqual(self.ol_up.tail.value, 1)
        self.ol_up.add(-2)
        self.assertEqual(self.ol_up.get_all(), [-2, 0, 1],
                         'Ошибка во время вставки в восходящий список из 2 элементов вниз')
        self.assertEqual(self.ol_up.head.value, -2)
        self.assertEqual(self.ol_up.tail.value, 1)
        self.ol_up.add(-1)
        self.assertEqual(self.ol_up.get_all(), [-2, -1, 0, 1],
                         'Ошибка во время вставки в восходящий список из 3 элементов между')
        self.assertEqual(self.ol_up.head.value, -2)
        self.assertEqual(self.ol_up.tail.value, 1)
        self.ol_up.add(-5)
        self.assertEqual(self.ol_up.get_all(), [-5, -2, -1, 0, 1],
                         'Ошибка во время вставки в восходящий список в голову')
        self.assertEqual(self.ol_up.head.value, -5)
        self.assertEqual(self.ol_up.tail.value, 1)
        self.ol_up.add(5)
        self.assertEqual(self.ol_up.get_all(), [-5, -2, -1, 0, 1, 5],
                         'Ошибка во время вставки в восходящий список в хвост')
        self.assertEqual(self.ol_up.head.value, -5)
        self.assertEqual(self.ol_up.tail.value, 5)

        # Тестирование нисходящего списка
        self.ol_dwn.add(0)
        self.assertEqual(self.ol_dwn.get_all(), [0], 'Ошибка во время вставки в пустой список')
        self.assertEqual(self.ol_dwn.head.value, 0)
        self.assertEqual(self.ol_dwn.tail.value, 0)
        self.ol_dwn.add(1)
        self.assertEqual(self.ol_dwn.get_all(), [1, 0],
                         'Ошибка во время вставки в нисходящий список из 1 элемента вниз')
        self.assertEqual(self.ol_dwn.head.value, 1)
        self.assertEqual(self.ol_dwn.tail.value, 0)
        self.ol_dwn.add(-2)
        self.assertEqual(self.ol_dwn.get_all(), [1, 0, -2],
                         'Ошибка во время вставки в нисходящий список из 2 элементов вверх')
        self.assertEqual(self.ol_dwn.head.value, 1)
        self.assertEqual(self.ol_dwn.tail.value, -2)
        self.ol_dwn.add(-1)
        self.assertEqual(self.ol_dwn.get_all(), [1, 0, -1, -2],
                         'Ошибка во время вставки в нисходящий список из 3 элементов между')
        self.assertEqual(self.ol_dwn.head.value, 1)
        self.assertEqual(self.ol_dwn.tail.value, -2)
        self.ol_dwn.add(-5)
        self.assertEqual(self.ol_dwn.get_all(), [1, 0, -1, -2, -5],
                         'Ошибка во время вставки в нисходящий список в хвост')
        self.assertEqual(self.ol_dwn.head.value, 1)
        self.assertEqual(self.ol_dwn.tail.value, -5)
        self.ol_dwn.add(5)
        self.assertEqual(self.ol_dwn.get_all(), [5, 1, 0, -1, -2, -5],
                         'Ошибка во время вставки в нисходящий список в голову')
        self.assertEqual(self.ol_dwn.head.value, 5)
        self.assertEqual(self.ol_dwn.tail.value, -5)

    def test_find(self):
        # Восходящий список
        self.assertIsNone(self.ol_up.find(1))
        self.ol_up.add(0)
        self.assertEqual(self.ol_up.find(0).value, 0)
        self.ol_up.add(-1)
        self.assertEqual(self.ol_up.find(0).value, 0)
        self.assertEqual(self.ol_up.find(-1).value, -1)

        # Нисходящий список
        self.assertIsNone(self.ol_dwn.find(1))
        self.ol_dwn.add(0)
        self.assertEqual(self.ol_dwn.find(0).value, 0)
        self.ol_dwn.add(1)
        self.assertEqual(self.ol_dwn.find(0).value, 0)
        self.assertEqual(self.ol_dwn.find(1).value, 1)

    def test_delete(self):
        # Восходящий список
        self.ol_up.delete(0)
        self.assertEqual(self.ol_up.get_all(), [])
        self.assertEqual([self.ol_up.head, self.ol_up.tail], [None, None])
        self.ol_up.add(0)
        self.ol_up.delete(0)
        self.assertEqual(self.ol_up.get_all(), [])
        self.assertEqual([self.ol_up.head, self.ol_up.tail], [None, None])
        self.ol_up.add(0)
        self.ol_up.add(1)
        self.ol_up.delete(0)
        self.assertEqual(self.ol_up.get_all(), [1])
        self.assertEqual([self.ol_up.head.value, self.ol_up.tail.value], [1, 1])
        self.ol_up.add(2)
        self.ol_up.add(3)
        self.ol_up.delete(2)
        self.assertEqual(self.ol_up.get_all(), [1, 3])
        self.assertEqual([self.ol_up.head.value, self.ol_up.tail.value], [1, 3])
        self.ol_up.delete(3)
        self.assertEqual(self.ol_up.get_all(), [1])
        self.assertEqual([self.ol_up.head.value, self.ol_up.tail.value], [1, 1])

        # Направсление списка не играет роли, поэтому с нисходящим работает также

    def test_clean(self):
        self.ol_up.add(1)
        self.ol_up.clean(True)
        self.assertEqual(self.ol_up.get_all(), [])

        self.ol_dwn.add(1)
        self.ol_dwn.clean(False)
        self.assertEqual(self.ol_dwn.get_all(), [])

    def test_len(self):
        self.assertEqual(self.ol_up.len(), 0)
        self.ol_up.add(1)
        self.assertEqual(self.ol_up.len(), 1)

    def test_get_all(self):
        self.assertEqual(self.ol_up.get_all(), [])
        self.ol_up.add(1)
        self.assertEqual(self.ol_up.get_all(), [1])
        self.ol_up.add(2)
        self.assertEqual(self.ol_up.get_all(), [1, 2])


class TestOrderedStringList(TestCase):
    def setUp(self):
        self.ol_up = OrderedStringList(True)
        self.ol_dwn = OrderedStringList(False)
        self.nd0 = Node('abc ')
        self.nd1 = Node(' bcd ')

    def test_compare(self):
        self.assertEqual(self.ol_up.compare(self.nd0, self.nd1), -1)
        self.assertEqual(self.ol_up.compare(self.nd1, self.nd0), 1)
        self.assertEqual(self.ol_up.compare(self.nd0, self.nd0), 0)
