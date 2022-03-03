import search
import unittest

class TestSearch(unittest.TestCase):
    def test_binary_search(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(search.binary_search(3, a), 2)
        self.assertIsNone(search.binary_search(0, a))
        self.assertIsNone(search.binary_search(7, a))

    def test_binary_search_first(self):
        a = [1, 2, 3, 3, 3, 3, 3, 5, 6]
        b = [3] * 10
        self.assertEqual(search.binary_search_first(3, a), 2)
        self.assertEqual(search.binary_search_first(3, b), 0)
        self.assertIsNone(search.binary_search_first(0, a))
        self.assertIsNone(search.binary_search_first(7, a))
        self.assertEqual(search.binary_search_first2(3, a), 2)
        self.assertEqual(search.binary_search_first2(3, b), 0)
        self.assertIsNone(search.binary_search_first2(0, a))
        self.assertIsNone(search.binary_search_first2(7, a))

    def test_kth_smallest(self):
        a = [6, 3, 2, 4, 5]
        self.assertEqual(search.kth_smallest(3, a), 4)
        self.assertEqual(search.kth_smallest(1, a), 2)
        self.assertEqual(search.kth_smallest(5, a), 6)

    def test_search_2d_array(self):
        a = [#0   1   2   3    4
            [-1,  2,  4,  5,   6],   # 0 
            [ 1,  5,  5,  9,   21],  # 1
            [ 3,  6,  6,  9,   22],  # 2
            [ 3,  6,  8,  10,  24],  # 3
            [ 6,  8,  9,  12,  25],  # 4 
            [ 8,  10, 12, 13,  40],  # 5
        ]
        self.assertFalse(search.search_2d_array(a, 7))
        self.assertTrue(search.search_2d_array(a, 8))
