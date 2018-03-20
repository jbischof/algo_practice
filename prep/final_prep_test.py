import unittest
import final_prep as fp
import numpy as np

class TestFinalPrep(unittest.TestCase):
  def testLongestTwoCharSubstring(self):
    self.assertEqual(fp.longest_twochar_substr('ababcbcbaaabbdef'),
                     'baaabb')
    self.assertEqual(fp.longest_Mchar_substr('ababcbcbaaabbdef', 2),
                     'baaabb')
    
  def testFindMOrderConnections(self):
    a = np.matrix([[0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1],
                   [0, 0, 0, 0, 1, 0]])

  def testIsDeckValid(self):
    deck = [1, 1, 2, 2, 3, 3, 3, 4, 5]
    self.assertTrue(fp.is_deck_valid(deck))
    # Remove one of needed 3s
    deck.pop(4)
    self.assertFalse(fp.is_deck_valid(deck))

