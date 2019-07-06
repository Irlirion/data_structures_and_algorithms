from unittest import TestCase
from data_structures.array.dyn_array import DynArray


class TestDynArray(TestCase):
    def test_insert(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        da.insert(0, 5)
        self.assertEqual([da[i] for i in range(len(da))], [5, 0, 1, 2, 3, 4])
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 6)

        da = DynArray()
        for i in range(1, 17):
            da.append(i)
        da.insert(0, 0)
        self.assertEqual([da[i] for i in range(len(da))], [i for i in range(17)])
        self.assertEqual(da.capacity, 32)

        self.assertRaises(IndexError, da.insert, 18, 18)

    def test_delete(self):
        da = DynArray()
        for i in range(4):
            da.append(i)
        da.delete(0)
        self.assertEqual([da[i] for i in range(len(da))], [1, 2, 3])
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 3)

        da = DynArray()
        for i in range(33):
            da.append(i)
        da.delete(0)
        da.delete(0)
        self.assertEqual([da[i] for i in range(len(da))], [i for i in range(2, 33)])
        self.assertEqual(da.capacity, 42)
        self.assertEqual(da.count, 31)

        da = DynArray()
        for i in range(3):
            da.append(i)
        da.delete(1)
        self.assertEqual([da[i] for i in range(len(da))], [0, 2])
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 2)

        da = DynArray()
        da.resize(18)
        for i in range(9):
            da.append(i)
        da.delete(0)
        self.assertEqual([da[i] for i in range(len(da))], [i for i in range(1, 9)])
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 8)

        self.assertRaises(IndexError, da.delete, 8)
