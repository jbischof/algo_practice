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
  
  def testPartitionObjArray(self):
    # TODO(bischof): improve test to only check partition is correct
    # This test imperfect because many object orders map on to a correct
    # partition.
    Greg = sorting.Person("Greg", 14)
    John = sorting.Person("John", 12)
    Andy = sorting.Person("Andy", 11)
    Jim = sorting.Person("Jim", 13)
    Phil = sorting.Person("Phil", 12)
    Bob = sorting.Person("Bob", 13)
    Chip = sorting.Person("Chip", 13)
    Tim = sorting.Person("Tim", 14)
    a = [Greg, John, Andy, Jim, Phil, Bob, Chip, Tim]
    sorting.partition_object_array(a, "age")
    self.assertEqual(a, [Andy, Phil, John, Chip, Jim, Bob, Greg, Tim])

