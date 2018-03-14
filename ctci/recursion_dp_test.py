"""Tests for recursion and dynamic programming problems."""

import recursion_dp as rdp
import unittest

class RecursionDPTest(unittest.TestCase):
  def testWaysToN(self):
    self.assertEqual(rdp.ways_to_n(2), 2)
    self.assertEqual(rdp.ways_to_n(3), 4)
    self.assertEqual(rdp.ways_to_n(4), 7)

  def testMazeRunner(self):
    maze = [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1]]
    path = rdp.maze_runner(maze)
    self.assertTrue(path) 
    # Should take west -> south path since backtrack north first
    self.assertEqual(
        path, 
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), 
         (2, 3), (3, 3), (4, 3), (4, 4)])
    # Cut off paths
    maze[4][0], maze[2][3] = 0, 0
    path = rdp.maze_runner(maze)
    self.assertFalse(path)

  def testMagicIndex(self):
    # Index `8` has value 8
    a = [-10, -8, -3, 1, 2, 3, 5, 6, 8, 10]
    self.assertEqual(rdp.magic_index(a), 8)
    # Remove match
    a[8] = 9
    self.assertEqual(rdp.magic_index(a), None)

  def testPowerSet(self):
    a = set([0, 1, 2])
    self.assertItemsEqual(
        rdp.power_set(a),
        [set([0, 1, 2]),
         set([0, 1]),
         set([0, 2]),
         set([1, 2]),
         set([0]),
         set([1]),
         set([2]),
         set([])])

  def testPermutations(self):
    self.assertItemsEqual(
        rdp.permutations('abc'),
        set(['abc', 'acb', 'cab', 'cba', 'bac', 'bca']))

  def testPermutationsNoDups(self):
    self.assertItemsEqual(
        rdp.permutations_no_dups('abc'),
        ['abc', 'acb', 'cab', 'cba', 'bac', 'bca'])
    self.assertItemsEqual(
        rdp.permutations_no_dups('aab'), ['aab', 'aba', 'baa'])

  def testAllParens(self):
    self.assertItemsEqual(
        rdp.all_parens(3),
        ['((()))', '(()())', '(())()', '()(())', '()()()'])
