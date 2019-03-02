import unittest
import graph

class TestGraph(unittest.TestCase):
  def defaultMaze(self):
    return  [[0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
             [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
             [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]]

  def simpleGraph(self):
    return graph.SimpleGraph(adj_list={
        'a': ['b', 'd', 'e'],
        'b': ['c', 'd'],
        'c': [],
        'd': ['a', 'e'],
        'e': [],
        })

  def testShortestMazeTraversal(self):
    self.assertEqual(
        len(graph.shortest_maze_traversal( 
            graph.Coordinate(9, 0), graph.Coordinate(0, 9),
            self.defaultMaze())),
        19)

  def testIsMazePath(self):
    self.assertTrue(
        graph.is_maze_path(graph.Coordinate(9, 0), graph.Coordinate(0, 9),
            self.defaultMaze()))
    # Remove access routes to exit
    maze = self.defaultMaze()
    maze[1][6], maze[2][7] = 0, 0
    self.assertFalse(
        graph.is_maze_path(graph.Coordinate(9, 0), graph.Coordinate(0, 9),
            maze))

  def testMazeTraversalDFS(self):
    path = graph.maze_traversal_dfs(
            graph.Coordinate(9, 0), graph.Coordinate(0, 9), self.defaultMaze())
    self.assertTrue(
        graph.maze_traversal_dfs(graph.Coordinate(9, 0), graph.Coordinate(0, 9),
            self.defaultMaze()))
    # Remove access routes to exit
    maze = self.defaultMaze()
    maze[1][6], maze[2][7] = 0, 0
    self.assertFalse(
        graph.maze_traversal_dfs(graph.Coordinate(9, 0), graph.Coordinate(0, 9),
            maze))

  def testIsConnected(self):
    g = self.simpleGraph()
    self.assertTrue(g.is_connected('b', 'a'))
    # Remove connection between 'd' and 'a'
    g.adj_list['d'] = ['e']
    self.assertFalse(g.is_connected('b', 'a'))

  def testShortestPath(self):
    g = self.simpleGraph()
    self.assertEqual(g.shortest_path('a', 'e'), ['a', 'e'])
    self.assertEqual(g.shortest_path('b', 'a'), ['b', 'd', 'a'])
    # Remove connection between 'd' and 'a'
    g.adj_list['d'] = ['e']
    self.assertFalse(g.shortest_path('b', 'a'))

  def testIsCyclic(self):
    g = graph.SimpleGraph(adj_list={
        'a': ['b', 'c'],
        'b': ['c', 'd', 'e'],
        'c': ['f'],
        'd': [],
        'e': [],
        'f': ['b'],
        'g': ['f', 'h'],
        'h': [],
        })
    self.assertTrue(g.is_cyclic())
    # Remove cyclic connection between 'f' and 'b'
    g.adj_list['f'] = []
    self.assertFalse(g.is_cyclic())
    # Add cycle in second tree
    g.adj_list['h'] = ['g']
    self.assertTrue(g.is_cyclic())

  def testTopologicalSort(self):
    g = graph.SimpleGraph(adj_list={
        'buy_ingredients': ['fry_sausage', 'boil_pasta', 'grate_cheese'],
        'fry_sausage': ['make_sauce'],
        'make_sauce': ['assemble_lasagna'],
        'boil_pasta': ['assemble_lasagna'],
        'grate_cheese': ['assemble_lasagna'],
        'assemble_lasagna': ['bake'],
        'bake': [],
        'wash_dishes': ['set_table'],
        'set_table': [],
        })
    self.assertEqual(
        g.topological_sort(),
        ['wash_dishes', 'set_table', 'buy_ingredients', 'grate_cheese',
         'boil_pasta', 'fry_sausage', 'make_sauce', 'assemble_lasagna', 'bake'])
