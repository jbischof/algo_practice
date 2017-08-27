import unittest
import recursion

class TestRecursion(unittest.TestCase):
  def testTowersOfHanoi(self):
    # Test mover function
    game = [[0, 1], [], []]
    moves = [] 
    recursion._toh_mover(game, moves, 0, 1)
    self.assertEqual(game, [[0], [1], []])
    recursion._toh_mover(game, moves, 0, 2)
    self.assertEqual(game, [[], [1], [0]])
    recursion._toh_mover(game, moves, 2, 1)
    self.assertEqual(game, [[], [1, 0], []])
    # Should raise exception if try to put larger plate on smaller one
    game = [[], [1], [0]]
    self.assertRaises(StandardError, recursion._toh_mover, game, moves, 1, 2)
    # Test main function
    moves, game = recursion.towers_of_hanoi(5)
    self.assertEqual(game, [[], range(4, -1, -1), []])

  def testAllPermutations(self):
    self.assertEqual(recursion.all_permutations(range(3)),
        [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]])

  def testPowerSet(self):
    self.assertEqual(recursion.power_set({0, 1, 2, 3}),
        [set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}, {0}, {0, 3},
         {0, 2}, {0, 2, 3}, {0, 1}, {0, 1, 3}, {0, 1, 2}, {0, 1, 2, 3}])
    self.assertEqual(recursion.power_set({1}), [set(), {1}])
    self.assertEqual(recursion.power_set(set()), [set()])

  def testAllSubsetsK(self):
    self.assertEqual(recursion.all_subsets_k({2, 3, 4, 5}, 3),
        [{3, 4, 5}, {2, 4, 5}, {2, 3, 4}, {2, 3, 5}])

  def testNQueens(self):
    self.assertEqual(recursion.n_queens(4), [[2, 4, 1, 3], [3, 1, 4, 2]])
