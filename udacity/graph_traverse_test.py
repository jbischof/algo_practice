import unittest
import graph_traverse

class TestGraphTraverse(unittest.TestCase):
	def ExampleGraph(self):
		graph = graph_traverse.Graph()
		graph.set_node_names((
					'Mountain View',   # 0
					'San Francisco',   # 1
					'London',          # 2
					'Shanghai',        # 3
					'Berlin',          # 4
					'Sao Paolo',       # 5
					'Bangalore'))      # 6 
		graph.insert_edge(51, 0, 1)     # MV <-> SF
		graph.insert_edge(51, 1, 0)     # SF <-> MV
		graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
		graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
		graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
		graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
		graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
		graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
		graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
		graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
		graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
		graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
		graph.insert_edge(932, 2, 4)    # London <-> Berlin
		graph.insert_edge(932, 4, 2)    # Berlin <-> London
		graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
		graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
		graph.insert_node(6)
		# (6) 'Bangalore' is intentionally disconnected (no edges)
		# for this problem and should produce None in the
		# Adjacency List, etc.
		return graph

	def testDFS(self):
		graph = self.ExampleGraph()
		self.assertEqual(
			graph.dfs_names(2), 
			['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin',
			'Sao Paolo'])

	def testBFS(self):
		graph = self.ExampleGraph()
		self.assertEqual(
			graph.bfs_names(2), 
			['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View',
			'San Francisco'])

	def testDijsktraPath(self):
		graph = self.ExampleGraph()
		# Start at London
		graph.find_node(3).node_from = graph.find_node(2)
		graph.find_node(4).node_from = graph.find_node(2)
		graph.find_node(5).node_from = graph.find_node(2)
		# Go to Berlin
		graph.find_node(1).node_from = graph.find_node(4)
		# Go to Shanghai
		graph.find_node(0).node_from = graph.find_node(3)
		self.assertEqual(graph.dijkstra_path(graph.find_node(3)), ['London', 'Shanghai'])	

	def testDijsktra(self):
		graph = self.ExampleGraph()
		self.assertEqual(graph.dijkstra(2, 3), (9217, ['London', 'Shanghai']))
		self.assertEqual(graph.dijkstra(4, 5), (10403, ['Berlin', 'London', 'Sao Paolo']))
		self.assertEqual(graph.dijkstra(0, 6), (float('Inf'), []))

if __name__ == '__main__':
		unittest.main()