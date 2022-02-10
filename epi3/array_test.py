import array
import unittest

class TestArray(unittest.TestCase):
    def test_sort_even_odd(self):
        a = [1, 7, 3, 9, 4, 5]
        array.sort_even_odd(a)
        self.assertListEqual(a, [4, 3, 9, 7, 1, 5])
