import unittest
import hash

class TestHash(unittest.TestCase):
  def testIsPalPerm(self):
    self.assertTrue(hash.is_palindrome_permuted("edified"))

  def testFindNearestRepeat(self):
    self.assertEqual(hash.find_nearest_repeat( 
      [5, 7, 11, 5, 2, 5, 6, 11, 7]), (3, 5))

  def testSmallestSubset(self):
    self.assertEqual(hash.find_smallest_match_subarray(
      [5, 4, 7, 8, 5, 11, 6, 4, 12, 1, 8, 2], [8, 4]), (1, 3))
    self.assertEqual(hash.find_smallest_match_subarray(
      [4, 7, 5, 11, 6, 12, 1, 8], [8, 4]), (0, 7))
