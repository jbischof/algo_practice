import unittest
import dp

class DPTest(unittest.TestCase):
  def testFib(self):
    self.assertEqual(dp.fib(0), 0)
    self.assertEqual(dp.fib(1), 1)
    self.assertEqual(dp.fib(5), 5)
    self.assertEqual(dp.fib(10), 55)

  def testCountScoreCombinations(self):
    self.assertEqual(dp.count_score_combinations([2, 3, 7], 12), 4)
    self.assertEqual(dp.count_score_combinations([7, 2, 3], 12), 4)

  def testEditDistance(self):
    self.assertEqual(dp.edit_distance('saturdays', 'sunday'), 4)
    self.assertEqual(dp.edit_distance('kitten', 'sitting'), 3)
    self.assertEqual(dp.edit_distance('carthorse', 'orchestra'), 8)
