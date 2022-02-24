import graph
import unittest
import copy

class TestGraph(unittest.TestCase):
    def test_find_maze_path(self):
        maze = [
            #    0  1  2  3  4
                [0, 0, 1, 1, 1], # 0
                [0, 1, 0, 1, 0], # 1
                [0, 0, 1, 1, 0], # 2
                [1, 1, 0, 1, 0], # 3
        ]
        self.assertFalse(graph.find_maze_path(
              copy.deepcopy(maze),
              (3, 0), (0, 4))[0])
        # Adding (2, 1) opens a path
        maze[2][1] = 1
        has_path, path = graph.find_maze_path(
                copy.deepcopy(maze),
                (3, 0), (0, 4))
        self.assertTrue(has_path)
        self.assertListEqual(path, 
                            [(3, 0), (3, 1), (2, 1), (2, 2), 
                             (2, 3), (1, 3), (0, 3), (0, 4)])

    def test_flood_fill(self):
        image = [
            #    0  1  2  3  4
                [0, 0, 1, 1, 1], # 0
                [0, 1, 0, 0, 0], # 1
                [0, 1, 1, 1, 0], # 2
                [1, 1, 0, 1, 0], # 3
        ]
        flood_fill_image = [
            #    0  1  2  3  4
                [0, 0, 1, 1, 1], # 0
                [0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0], # 3
        ]
        graph.flood_fill(image, (2, 1))
        for row in range(len(image)):
            self.assertListEqual(image[row], flood_fill_image[row])
