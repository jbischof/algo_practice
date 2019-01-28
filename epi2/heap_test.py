import unittest
import heap

class HeapTest(unittest.TestCase):
  def testMergedSortedLists(self):
    lists = [[1, 4, 7], [2, 4, 6], [5, 9, 10]]
    self.assertEqual(heap.merge_sorted_lists(lists),
                     [1, 2, 4, 4, 5, 6, 7, 9, 10])

  def testContainerWithMedian(self):
    a = [1, 0, 3, 5, 2, 0, 1]
    expect_medians = [1, 0.5, 1, 2, 2, 1.5, 1]
    cwm = heap.ContainerWithMedian()
    for i in range(len(a)):
      cwm.append(a[i])
      self.assertEqual(cwm.median(), expect_medians[i])
    
