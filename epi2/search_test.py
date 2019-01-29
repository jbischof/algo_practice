"""Testing search"""
import unittest
import search

class SearchTest(unittest.TestCase):
  def testFindFirst(self):
    a = [0, 0, 1, 1, 1, 2, 3, 3, 4]
    self.assertEqual(search.find_first(a, 1), 2)
    self.assertEqual(search.find_first(a, 0), 0)
    self.assertEqual(search.find_first(a, 5), None)

  def testBisectSqrt(self):
    self.assertAlmostEqual(search.bisect_sqrt(9), 3)
    self.assertAlmostEqual(search.bisect_sqrt(1/float(9)), 1/float(3))
    self.assertAlmostEqual(search.bisect_sqrt(0), 0)

  def testPivotArray(self):
    a = [4, 2, 0, 5, 3, 6, 1]
    self.assertEqual(search.pivot_array(a, 0, len(a) - 1), 1)
    self.assertEqual(a[0], 0)
    self.assertEqual(set(a[2:]), set([2, 3, 4, 5, 6]))

  def quickselect(self):
    a = [4, 2, 0, 5, 3, 6, 1]
    self.assertEqual(array.quickselect(3), 3)
    a = [4, 2, 0, 5, 3, 6, 1]
    self.assertEqual(array.quickselect(6), 6)
