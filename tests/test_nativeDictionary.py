from unittest import TestCase
from data_structures.set.NativeDictionary import NativeDictionary


class TestNativeDictionary(TestCase):
    def setUp(self):
        self.sz = 10
        self.d = NativeDictionary(self.sz)

    def test_is_key(self):
        self.d.put('1', 1)
        self.assertTrue(self.d.is_key('1'))
        self.assertIn('1', self.d.slots)
        self.assertIn(1, self.d.values)
        self.assertEqual(self.d.slots.index('1'), self.d.values.index(1))

        self.d.put('1', 2)
        self.assertTrue(self.d.is_key('1'))
        self.assertIn('1', self.d.slots)
        self.assertIn(1, self.d.values)
        self.assertEqual(self.d.slots.index('1'), self.d.values.index(1))

        self.assertFalse(self.d.is_key('2'))

    def test_put(self):
        self.d.put('1', 1)
        self.assertIn('1', self.d.slots)
        self.assertIn(1, self.d.values)
        self.assertEqual(self.d.slots.index('1'), self.d.values.index(1))

        self.d.put('1', 2)
        self.assertIn('1', self.d.slots)
        self.assertIn(1, self.d.values)
        self.assertEqual(self.d.slots.index('1'), self.d.values.index(1))

    def test_get(self):
        for i in range(self.sz):
            self.d.put(str(i), i)
        for i in range(self.sz):
            with self.subTest(i=i):
                self.assertEqual(self.d.get(str(i)), i)
