import unittest
import final_prep

class TestFinalPrep(unittest.TestCase):
  def testLongestTwoCharSubstring(self):
    self.assertEqual(final_prep.longest_twochar_substr('ababcbcbaaabbdef'),
                     'baaabb')
    self.assertEqual(final_prep.longest_Mchar_substr('ababcbcbaaabbdef', 2),
                     'baaabb')
