import unittest
import sort

class TestSort(unittest.TestCase):
  def testArrayIntersect(self):
    a = [2, 3, 3, 5, 7, 11]
    b = [3, 3, 7, 15, 31]
    self.assertEqual(sort.array_intersect(a, b), [3, 7])

  def testMergeSortedArrays(self):
    a = [2, 3, 3, 5, 7, 11]
    b = [3, 3, 7, 15, 31]
    sort.merge_sorted_arrays(a, b)
    self.assertEqual(a, [2, 3, 3, 3, 3, 5, 7, 7, 11, 15, 31])

  def testMaxEventOverlap(self):
    self.assertEqual(sort.max_event_overlap([]), 0)
    self.assertEqual(sort.max_event_overlap([
        sort.Event(0, 5),
        sort.Event(6, 7),
        sort.Event(8, 10),
        sort.Event(13, 15)]), 1)
    self.assertEqual(sort.max_event_overlap([
        sort.Event(0, 5),
        sort.Event(2, 7),
        sort.Event(8, 10),
        sort.Event(13, 15)]), 2)
    self.assertEqual(sort.max_event_overlap([
        sort.Event(0, 5),
        sort.Event(2, 7),
        sort.Event(8, 10),
        sort.Event(8, 10),
        sort.Event(9, 11),
        sort.Event(9, 12),
        sort.Event(13, 15)]), 4)

  def testMergeDisjointEvents(self):
    events = [sort.Event(-4 , -1), sort.Event(0, 2), sort.Event(3, 6), 
              sort.Event(7, 9), sort.Event(11, 12), sort.Event(14, 17)] 
    new_event = sort.Event(1, 8)
    expect_events = [sort.Event(-4 , -1), sort.Event(0, 9), sort.Event(11, 12),
                     sort.Event(14, 17)] 
    self.assertEqual(sort.merge_disjoint_events(events, new_event), 
                     expect_events)
