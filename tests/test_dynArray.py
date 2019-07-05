from unittest import TestCase
from data_structures.array.dyn_array import DynArray


class TestDynArray(TestCase):
    def test_insert(self):
        da = DynArray()
        da.insert(0, 1)
        self.assertEqual(da[0], 1)

        da.append(2)
        da.append(4)
        da.insert(2, 3)
        self.assertEqual(da[2], 3)
        self.assertEqual(da[3], 4)

        da = DynArray()
        for i in range(0, 16):
            da.append(i)
        da.insert(16, 16)
        self.assertEqual(da[16], 16)

    def test_delete(self):
        da = DynArray()
        for i in range(0, 48):
            da.append(i)
        for i in range(0, 25):
            da.delete(0)
        self.assertEqual(da[0], 25)
