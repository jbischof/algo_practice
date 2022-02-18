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
