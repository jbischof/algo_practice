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

  def testPartition(self):
    a = [2, 5, 7, 11, 3, 15, 9]
    self.assertEqual(search.partition(a, 0, len(a) - 1), 4)
    self.assertEqual(a, [2, 5, 7, 3, 9, 15, 11])
    a = [3, 5, 2, 7, 6, 11, 1, 17, 0]
    self.assertEqual(search.partition(a, 0, len(a) - 1), 0)
    self.assertEqual(a, [0, 5, 2, 7, 6, 11, 1, 17, 3])

  def testFindKSmallest(self):
    a = [3, 5, 2, 7, 6, 11, 1, 17, 0]
    self.assertEqual(search.find_kth_smallest(a, 3), 2)
    self.assertEqual(search.find_kth_smallest(a, 0), 0)
    self.assertEqual(search.find_kth_smallest(a, 9), 17)

  def testFindMissingInt(self):
    input_ints = range(256)
    input_ints.pop()
    self.assertEqual(search.find_missing_8bit_int(input_ints), 255)
    input_ints = range(256)
    input_ints.pop(23)
    self.assertEqual(search.find_missing_8bit_int(input_ints), 23) 
    input_ints = range(256)
    self.assertRaises(ValueError, search.find_missing_8bit_int, input_ints)
