import unittest
import final_prep as fp
import numpy as np

class TestFinalPrep(unittest.TestCase):
  def testLongestTwoCharSubstring(self):
    self.assertEqual(fp.longest_twochar_substr('ababcbcbaaabbdef'),
                     'baaabb')
    self.assertEqual(fp.longest_Mchar_substr('ababcbcbaaabbdef', 2),
                     'baaabb')

  def testIsDeckValid(self):
    deck = [1, 1, 2, 2, 3, 3, 3, 4, 5]
    self.assertTrue(fp.is_deck_valid(deck))
    # Remove one of needed 3s
    deck.pop(4)
    self.assertFalse(fp.is_deck_valid(deck))

  def testIsRoot(self):
    # A genuine tree
    adj_list = {
        'a': set('bc'),
        'b': set('de'),
        'c': set('f'),
        'd': set(),
        'e': set(),
        'f': set()
    }
    self.assertTrue(fp.is_tree(adj_list))
    # Add cycle
    adj_list['c'].add('e')
    self.assertFalse(fp.is_tree(adj_list))
    adj_list['c'].remove('e')
    # Add other tree
    adj_list['g'] = set('hi')
    adj_list['h'] = set()
    adj_list['i'] = set()
    self.assertFalse(fp.is_tree(adj_list))

  def testIsSubsetSum(self):
    self.assertTrue(fp.is_subset_sum([8, 6, 7, 5, 3, 10, 9], 15))
    self.assertFalse(fp.is_subset_sum([11, 6, 5, 1, 7, 13, 12], 15))
    self.assertTrue(fp.is_subset_sum([11, 6, 5, 1, 7, 13, 15], 15))

  def testPartitionArrayWeight(self):
    a = [5, 6, 11, 20, 3, 11, 6, 10, 2, 2, 1]
    self.assertEqual(fp._partition_array_weight(a, 4, 22), [
        fp.Partition(2, 22),
        fp.Partition(3, 20),
        fp.Partition(6, 20),
        fp.Partition(10, 15)])
    self.assertFalse(fp._partition_array_weight(a, 4, 21))
    self.assertEqual(fp.min_cargo_capacity(a, 4), 22)
