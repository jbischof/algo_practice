import heaps
import unittest

class TestHeaps(unittest.TestCase):
  def testMergeSortedArrays(self):
    self.assertEqual(
      heaps.merge_sorted_arrays([[0, 1, 2], [2, 3, 4], [4, 5, 6]]),
      [0, 1, 2, 2, 3, 4, 4, 5, 6])

  def testSortKSorted(self):
    self.assertEqual(heaps.sort_k_sorted([1, 0, 3, 2, 4], 1), [0, 1, 2, 3, 4])
    self.assertEqual(heaps.sort_k_sorted([1, 0, 3, 2, 4], 5), [0, 1, 2, 3, 4])

  def testKSmallest(self):
    self.assertEqual(heaps.k_smallest([8, 4, 5, 6, 3, 2], 3), [2, 3, 4])
    self.assertEqual(heaps.k_smallest([8, 4, 5, 6, 3, 2], 7), [2, 3, 4, 5, 6, 8])
