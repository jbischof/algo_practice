import unittest
import search

class TestSearch(unittest.TestCase):
  def testFindFirst(self):
    a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    self.assertEqual(search.find_first(a, -14), 0)
    self.assertEqual(search.find_first(a, 108), 3)
    self.assertEqual(search.find_first(a, 285), 6)
    self.assertEqual(search.find_first(a, 401), 9)

  def testFindMinCyclic(self):
    self.assertEqual(search.find_min_cyclic_sorted(
        [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]), 4)
    self.assertEqual(search.find_min_cyclic_sorted(
        [17, 19, 21, 0, 5, 7, 9, 11, 15]), 3)
    self.assertEqual(search.find_min_cyclic_sorted(
        [17, 21, 25, 30, 35, 37, 41, 50, 55, 0, 15]), 9)
    self.assertEqual(search.find_min_cyclic_sorted(
        [17, 21, 25, 30, 35, 37, 41, 50, 55, 0]), 9)
    self.assertEqual(search.find_min_cyclic_sorted(
        [0, 17, 21, 25, 30, 35, 37, 41, 50, 55]), 0)

  def testIntSqrt(self):
    self.assertEqual(search.int_sqrt(9), 3)
    self.assertEqual(search.int_sqrt(10), 3)
    self.assertEqual(search.int_sqrt(1), 1)

  def testSearch2D(self):
    a = [[-1, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9, 22],
         [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]]
    self.assertFalse(search.search_2d(a, 7))
    self.assertTrue(search.search_2d(a, 8))
    self.assertTrue(search.search_2d(a, 12))
    self.assertFalse(search.search_2d(a, -10))
    self.assertFalse(search.search_2d(a, 50))
