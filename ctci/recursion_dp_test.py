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
