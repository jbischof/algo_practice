import unittest
import dp

class DPTest(unittest.TestCase):
  def testMaxSubarray(self):
    self.assertEqual(dp.max_subarray(
        [904, 40, 523, 12, -335, -385, -124, 481, -31]), (0, 3))
    self.assertEqual(dp.max_subarray(
        [-130, 904, 40, 523, 12, -335, -385, -124, 481]), (1, 4))
    # Only one positive entry at a time
    self.assertEqual(dp.max_subarray(
        [904, -40, -523, -12, -335, -385, -124, 481, -31]), (0, 0))
    self.assertEqual(dp.max_subarray(
        [4, -40, -523, -12, -335, -385, -124, 481, -31]), (7, 7))

  def testScoreCombs(self):
    self.assertEqual(dp.score_combs(12, (2, 3, 7)), 4)

  def testHighestValuePath(self):
    sea = [
        [0,  2,  0,  0,  0,  0],
        [0,  0,  5,  0,  3,  0],
        [0,  2,  0,  0,  0, 10],
        [5,  0,  0, 10,  0,  0],
        [0, 10,  0,  0,  0, 10],
        [5,  0,  0,  0,  0,  2]]
    self.assertEqual(dp.highest_value_path(sea), 32)

  def testChoose(self):
    self.assertEqual(dp.choose(8, 3), 56)
    self.assertEqual(dp.choose(8, 0), 1)
    self.assertEqual(dp.choose(8, 8), 1)
    self.assertEqual(dp.choose_float(8, 3), 56)
    self.assertEqual(dp.choose_float(8, 0), 1)
    self.assertEqual(dp.choose_float(8, 8), 1)
