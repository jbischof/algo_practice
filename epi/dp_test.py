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

  def testCountArrayTraversals(self):
    self.assertEqual(dp.count_array_traversals(5, 5), 70)
    self.assertEqual(dp.count_array_traversals(5, 10), 715)

  def testKnapsack(self):
    items = [dp.Item('A', 20, 65),
             dp.Item('B', 8, 35),
             dp.Item('C', 60, 245),
             dp.Item('D', 55, 195),
             dp.Item('E', 40, 65),
             dp.Item('F', 70, 150),
             dp.Item('G', 85, 275),
             dp.Item('H', 25, 155),
             dp.Item('I', 30, 120),
             dp.Item('J', 65, 320),
             dp.Item('K', 75, 75),
             dp.Item('L', 10, 40),
             dp.Item('M', 95, 200),
             dp.Item('N', 50, 100),
             dp.Item('O', 40, 220),
             dp.Item('P', 10, 99)]
    self.assertEqual(dp.knapsack(items, 130), 695)
