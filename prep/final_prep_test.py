import unittest
import final_prep
import numpy as np

class TestFinalPrep(unittest.TestCase):
  def testLongestTwoCharSubstring(self):
    self.assertEqual(final_prep.longest_twochar_substr('ababcbcbaaabbdef'),
                     'baaabb')
    self.assertEqual(final_prep.longest_Mchar_substr('ababcbcbaaabbdef', 2),
                     'baaabb')
    
  def testFindMOrderConnections(self):
    a = np.matrix([[0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1],
                   [0, 0, 0, 0, 1, 0]])
