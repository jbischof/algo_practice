import unittest
import recursion as rn

class TestRecursion(unittest.TestCase):
  def testGCD(self):
    self.assertEqual(rn.gcd(32, 16), 16)
    self.assertEqual(rn.gcd(33, 12), 3)
    self.assertEqual(rn.gcd(33, 1), 1)

  def testGCDRN(self):
    self.assertEqual(rn.gcd_nr(32, 16), 16)
    self.assertEqual(rn.gcd_nr(33, 12), 3)
    self.assertEqual(rn.gcd_nr(33, 1), 1)

  def testTowersOfHanoi(self):
    self.assertEqual([[], [3, 2, 1, 0], []], rn.towers_of_hanoi(4))

  def testPermutations(self):
    self.assertItemsEqual(
        rn.permutations([1, 2, 3]),
        [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1], [3, 1, 2]])
    self.assertItemsEqual(
        rn.permutations_nr([1, 2, 3]),
        [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1], [3, 1, 2]])

  def testAllSubsets(self):
    self.assertItemsEqual(rn.all_subsets([1, 2, 3, 4], 2),
        [{1, 2}, {1, 3}, {2, 3}, {1, 4}, {2, 4}, {3, 4}]) 

  def testIsPalindrome(self):
    self.assertTrue(rn.is_palindrome('2'))
    self.assertTrue(rn.is_palindrome('22'))
    self.assertTrue(rn.is_palindrome('202'))
    self.assertTrue(rn.is_palindrome('32023'))
    self.assertFalse(rn.is_palindrome('23'))
    self.assertFalse(rn.is_palindrome('203'))
    self.assertFalse(rn.is_palindrome('320234'))

  def testPalDecomps(self):
    expect_decomp = [
        ['0', '2', '0', '4', '4', '5', '1', '8', '8', '1'],
        ['0', '2', '0', '4', '4', '5', '1', '88', '1'], 
        ['0', '2', '0', '4', '4', '5', '1881'],
        ['0', '2', '0', '44', '5', '1', '8', '8', '1'],
        ['0', '2', '0', '44', '5', '1', '88', '1'], 
        ['0', '2', '0', '44', '5', '1881'],
        ['020', '4', '4', '5', '1', '8', '8', '1'],
        ['020', '4', '4', '5', '1', '88', '1'],
        ['020', '4', '4', '5', '1881'],
        ['020', '44', '5', '1', '8', '8', '1'],
        ['020', '44', '5', '1', '88', '1'],
        ['020', '44', '5', '1881']]
    self.assertItemsEqual(rn.palindrome_decomps('0204451881'), expect_decomp) 
    self.assertItemsEqual(rn.palindrome_decomps2('0204451881'), expect_decomp) 
