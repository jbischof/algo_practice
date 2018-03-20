"""Tests for searching and sorting algorithms."""

import search_sort as ss
import unittest

class TestSearchSort(unittest.TestCase):
  def testMergeSortedArrays(self):
    # Normal case
    a = [5, 10, 15, 17]
    b = [0, 7, 11, 20]
    ss.merge_sorted_arrays(a, b)
    self.assertEqual(a, [0, 5, 7, 10, 11, 15, 17, 20])
    # A is strictly larger
    a = [5, 6, 7, 8]
    b = [0, 2, 4]
    ss.merge_sorted_arrays(a, b)
    self.assertEqual(a, [0, 2, 4, 5, 6, 7, 8])
    # B is strictly larger
    a = [0, 2, 4]
    b = [5, 6, 7, 8]
    ss.merge_sorted_arrays(a, b)
    self.assertEqual(a, [0, 2, 4, 5, 6, 7, 8])

  def testBinarySearchRotated(self):
    a = range(9)
    end_a = len(a) - 1
    five_pos = 5
    for j in xrange(9):
      # Move one item from front to back
      ans = ss.binary_search_rotated(a, 5)
      self.assertEqual(ans, (five_pos % len(a)))
      a = [a[end_a]] + a[: end_a]
      five_pos += 1
