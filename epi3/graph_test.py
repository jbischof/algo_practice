import graph
import unittest
import copy
from graph import Node, Edge

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

    def test_has_cycle(self):
        """

                 A------\
              ^     \    \
             /       v    v 
             D       B -> C
             ^      /      \
              \    v        v
                E           F

        """
        g = {
            'A': ['B'],
            'B': ['C', 'E'],
            'C': ['F'],
            'D': ['A'],
            'E': ['D'],
            'F': [],
        }
        self.assertTrue(graph.has_cycle(g))
        # Remove back edge between D and A
        g['D'] = []
        self.assertFalse(graph.has_cycle(g))
        # Check that OK if two nodes pointing to same child without cycle
        g['A'].append('C')
        self.assertFalse(graph.has_cycle(g))

    def test_topo_sort(self):
        g = {
            'a': ['b', 'f'],
            'b': ['c', 'd', 'f'],
            'c': ['d'],
            'd': ['e', 'f'],
            'e': ['f'],
            'f': [],
        }
        res1 = graph.topo_sort(g)
        self.assertTrue(res1[0])
        self.assertListEqual(res1[1], ['a', 'b', 'c', 'd', 'e', 'f'])
        # Add a backlink between 'f' and 'b'
        g['f'].append('a')
        self.assertFalse(graph.topo_sort(g)[0])

    def test_is_bipartite(self):
        g = {
            1: [4, 5, 6],
            2: [4, 6],
            3: [5, 6],
            4: [1, 2],
            5: [1, 3],
            6: [1, 2, 3],
        }
        res1 = graph.is_bipartite(g)
        self.assertTrue(res1[0])
        # Make second bipartite set
        g[7] = [8, 9]
        g[8] = [7]
        g[9] = [7]
        res2 = graph.is_bipartite(g)
        self.assertTrue(res2[0])
        # Violate bipartite relation
        g[5].append(6)
        g[6].append(5)
        res3 = graph.is_bipartite(g)
        self.assertFalse(res3[0])

    def test_dijkstra(self):
        reyk = Node("reyk")
        oslo = Node("oslo")
        london = Node("london")
        berlin = Node("berlin")
        rome = Node("rome")
        moscow = Node("moscow")
        belgrade = Node("belgrade")
        athens = Node("athens")
        reyk.edges = [
                Edge(5, oslo),
                Edge(4, london),
        ]
        oslo.edges = [
                Edge(5, reyk),
                Edge(3, moscow),
                Edge(1, berlin),
        ]
        london.edges = [
                Edge(4, reyk),
                Edge(3, berlin),
        ]
        berlin.edges = [
                Edge(1, oslo),
                Edge(9, belgrade),
                Edge(2, rome),
                Edge(3, london),
        ]
        rome.edges = [
                Edge(2, berlin),
                Edge(2, athens),
        ]
        moscow.edges = [
                Edge(3, oslo),
                Edge(5, belgrade),
                Edge(4, athens),
        ]
        belgrade.edges = [
                Edge(9, berlin),
                Edge(1, athens),
                Edge(5, moscow),
        ]
        athens.edges = [
                Edge(2, rome),
                Edge(1, belgrade),
                Edge(4, moscow),
        ]
        res = graph.dijkstra(reyk, belgrade)
        self.assertEqual(res[0], 11)
        self.assertListEqual(
                res[1], 
                ['reyk', 'oslo', 'berlin', 'rome', 'athens', 'belgrade']
        ) 

