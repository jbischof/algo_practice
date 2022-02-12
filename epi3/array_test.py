import array
import unittest

class TestArray(unittest.TestCase):
    def test_sort_even_odd(self):
        a = [1, 7, 3, 9, 4, 5]
        array.sort_even_odd(a)
        self.assertListEqual(a, [4, 3, 9, 7, 1, 5])

    def test_increment_int(self):
        a = [1, 2, 3]
        array.increment_int(a)
        self.assertListEqual(a, [1, 2, 4])
        a = [1, 9, 9]
        array.increment_int(a)
        self.assertListEqual(a, [2, 0, 0])
        a = [9, 9, 9]
        array.increment_int(a)
        self.assertListEqual(a, [1, 0, 0, 0])

    def test_del_dups(self):
        a = [2, 5, 3, 2, 6, 5]
        array.del_dups(a)
        self.assertListEqual(a, [2, 5, 3, 6, 0, 0])
        a = [2, 5, 3, 2, 5, 6]
        array.del_dups(a)
        self.assertListEqual(a, [2, 5, 3, 6, 0, 0])

    def test_len_longest_equal_subarray(self):
        a = [3, 3, 4, 5, 5, 5, 6]
        self.assertEqual(array.len_longest_equal_subarray(a), 3)
        a = [1, 7, 3, 9, 4, 5]
        self.assertEqual(array.len_longest_equal_subarray(a), 1)
        
    def test_subarray_sum(self):
        a = [1, 5, 3, 7, 6]
        self.assertFalse(array.subarray_sum(a, 11))
        self.assertTrue(array.subarray_sum(a, 10))
        self.assertTrue(array.subarray_sum(a, 3))
