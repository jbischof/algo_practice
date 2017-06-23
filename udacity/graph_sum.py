class Node(object):
	def __init__(self, value):
		self.value = value
		self.edges = []

class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def insert_node(self, new_node_val):
		new_node = Node(new_node_val)
		self.nodes.append(new_node)
		
	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None
		to_found = None
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node
		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)
		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)
		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)

	def max_index(self):
		max = 0
		for edge in self.edges:
			if edge.node_from.value > max:
				max = edge.node_from.value
			if edge.node_to.value > max:
				max = edge.node_to.value
		return max

	def get_edge_list(self):
		"""Don't return a list of edge objects!
		Return a list of triples that looks like this:
		(Edge Value, From Node Value, To Node Value)"""
		return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

	def get_adjacency_list(self):
		"""Don't return any Node or Edge objects!
		You'll return a list of lists.
		The indicies of the outer list represent "from" nodes.
		Each section in the list will store a list of tuples that looks like this:
		(To Node, Edge Value)"""
		ret = [None] * (self.max_index() + 1)
		for edge in self.edges:
			from_val = edge.node_from.value
			if ret[from_val] is None:
				ret[from_val] = []
			ret[from_val].append((edge.node_to.value, edge.value))
		return ret

	def get_adjacency_matrix(self):
		"""Return a matrix, or 2D list.
		Row numbers represent from nodes, column numbers represent to nodes.
		Store the edge values in each spot, and a 0 if no edge exists."""
		n_nodes = self.max_index() + 1
		ret = [[0 for i in range(n_nodes)] for j in range(n_nodes)]
		for edge in self.edges:
			ret[edge.node_from.value][edge.node_to.value] = edge.value
		return ret
