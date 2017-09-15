import unittest
import graph


class TestGraph(unittest.TestCase):
  
  def testMazeTraversalShortest(self):
    maze = [[0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]]
    self.assertEqual(
        graph.maze_traverse_shortest(maze), 
        [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5),
         (6, 6), (5, 6), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9),
         (0, 9)])

  def testFloodFill(self):
    image = [[1, 1, 1, 1, 0, 1, 1, 1, 0],
             [0, 1, 1, 0, 1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 1, 0, 0, 1],
             [0, 0, 1, 1, 0, 0, 1, 1, 1],
             [0, 1, 1, 1, 1, 0, 1, 0, 0],
             [0, 1, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 1, 1]]
    expect_image = [[0, 0, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 1, 1]]
    graph.flood_fill(image, (3, 2))
    self.assertEqual(image, expect_image)

  def testStringPathTransform(self):
    a, b = 'cat', 'dog'
    str_set = {a, b, 'bat', 'cot', 'bag', 'dag', 'dot', 'can', 'fog', 'doh'}
    self.assertEqual(graph.string_path_transform(a, b, str_set),
                     ['cat', 'bat', 'bag', 'dag', 'dog'])
