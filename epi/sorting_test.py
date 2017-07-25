import unittest
import sorting

class TestSorting(unittest.TestCase):
  def testMergeSortedArrays(self):
    a = [2, 5, 10, 11, 11, 11, 17]
    b = [11, 12, 13, 14, 16, 19, 20]
    sorting.merge_sorted_arrays(a, b)
    self.assertEqual(a, [2, 5, 10, 11, 11, 11, 11, 12, 13, 14, 16, 17, 19, 20])

  def testMaxEventOverlap(self):
    self.assertEqual(sorting.event_max_overlap([]), 0)
    self.assertEqual(sorting.event_max_overlap([
        sorting.Event(0, 5),
        sorting.Event(6, 7),
        sorting.Event(8, 10),
        sorting.Event(13, 15)]), 1)
    self.assertEqual(sorting.event_max_overlap([
        sorting.Event(0, 5),
        sorting.Event(2, 7),
        sorting.Event(8, 10),
        sorting.Event(13, 15)]), 2)
    self.assertEqual(sorting.event_max_overlap([
        sorting.Event(0, 5),
        sorting.Event(2, 7),
        sorting.Event(8, 10),
        sorting.Event(8, 10),
        sorting.Event(9, 11),
        sorting.Event(9, 12),
        sorting.Event(13, 15)]), 4)
