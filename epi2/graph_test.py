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

  def testClosestXYPair(self):
    a = [['x', 'a', 'a', 'a', 'y', 'a'],
         ['a', 'x', 'a', 'a', 'a', 'a'],
         ['x', 'a', 'a', 'y', 'a', 'a'],
         ['a', 'a', 'a', 'a', 'a', 'a'],
         ['a', 'a', 'y', 'a', 'a', 'x']] 
    self.assertEqual(graph.closest_XY_pair(a), 3)

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

  def testMinSpanTree(self):
    g = graph.Graph(adj_list={
        'a': [
            graph.Edge('a', 'b', 2),
            graph.Edge('a', 'f', 2),
            graph.Edge('a', 'd', 7)],
        'b': [
            graph.Edge('b', 'a', 2),
            graph.Edge('b', 'f', 5),
            graph.Edge('b', 'c', 1),
            graph.Edge('b', 'e', 3)],
        'c': [
            graph.Edge('c', 'b', 1),
            graph.Edge('c', 'e', 4),
            graph.Edge('c', 'f', 4)],
        'd': [
            graph.Edge('d', 'a', 7),
            graph.Edge('d', 'e', 1),
            graph.Edge('d', 'g', 5)],
        'e': [
            graph.Edge('e', 'b', 3),
            graph.Edge('e', 'c', 4),
            graph.Edge('e', 'd', 1),
            graph.Edge('e', 'g', 7)],
        'f': [
            graph.Edge('f', 'a', 2),
            graph.Edge('f', 'b', 5),
            graph.Edge('f', 'c', 4)],
        'g': [
            graph.Edge('g', 'd', 5),
            graph.Edge('g', 'e', 7)]})
    mst_edges = graph.min_span_tree(g)
    edge_sets = [set([edge.source, edge.dest]) for edge in mst_edges]
    self.assertItemsEqual(edge_sets, [
        set(['a', 'f']),
        set(['a', 'b']),
        set(['b', 'c']),
        set(['b', 'e']),
        set(['e', 'd']),
        set(['g', 'd'])])
