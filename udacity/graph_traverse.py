class Node(object):
	def __init__(self, value):
		self.value = value
		self.edges = []
		self.visited = False
		self.distance = float('Inf')
		self.node_from = None

class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
	def __init__(self, nodes=None, edges=None):
		self.nodes = nodes or []
		self.edges = edges or []
		self.node_names = []
		self._node_map = {}

	def set_node_names(self, names):
		"""The Nth name in names should correspond to node number N.
		Node numbers are 0 based (starting at 0).
		"""
		self.node_names = list(names)

	def insert_node(self, new_node_val):
		"Insert a new node with value new_node_val"
		new_node = Node(new_node_val)
		self.nodes.append(new_node)
		self._node_map[new_node_val] = new_node
		return new_node

	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		# Insert a new edge, creating new nodes if necessary
		nodes = {node_from_val: None, node_to_val: None}
		# Check for edge nodes in graph object
		for node in self.nodes:
			if node.value in nodes:
				nodes[node.value] = node
				if all(nodes.values()):
					break
		# Insert any nodes not already present in graph object
		for node_val in nodes:
			nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
		# Create and insert edge object to graph object
		node_from = nodes[node_from_val]
		node_to = nodes[node_to_val]
		new_edge = Edge(new_edge_val, node_from, node_to)
		node_from.edges.append(new_edge)
		node_to.edges.append(new_edge)
		self.edges.append(new_edge)

	def get_edge_list(self):
		"""Return a list of triples that looks like this:
		(Edge Value, From Node, To Node)"""
		return [(e.value, e.node_from.value, e.node_to.value)
				for e in self.edges]

	def get_edge_list_names(self):
		"""Return a list of triples that looks like this:
		(Edge Value, From Node Name, To Node Name)"""
		return [(edge.value,
				 self.node_names[edge.node_from.value],
				 self.node_names[edge.node_to.value])
				for edge in self.edges]

	def get_adjacency_list(self):
		"""Return a list of lists.
		The indecies of the outer list represent "from" nodes.
		Each section in the list will store a list
		of tuples that looks like this:
		(To Node, Edge Value)"""
		max_index = self.find_max_index()
		adjacency_list = [[] for _ in range(max_index)]
		for edg in self.edges:
			from_value, to_value = edg.node_from.value, edg.node_to.value
			adjacency_list[from_value].append((to_value, edg.value))
		return [a or None for a in adjacency_list] # replace []'s with None

	def get_adjacency_list_names(self):
		"""Each section in the list will store a list
		of tuples that looks like this:
		(To Node Name, Edge Value).
		Node names should come from the names set
		with set_node_names."""
		adjacency_list = self.get_adjacency_list()
		def convert_to_names(pair, graph=self):
			node_number, value = pair
			return (graph.node_names[node_number], value)
		def map_conversion(adjacency_list_for_node):
			if adjacency_list_for_node is None:
				return None
			return map(convert_to_names, adjacency_list_for_node)
		return [map_conversion(adjacency_list_for_node)
				for adjacency_list_for_node in adjacency_list]

	def get_adjacency_matrix(self):
		"""Return a matrix, or 2D list.
		Row numbers represent from nodes,
		column numbers represent to nodes.
		Store the edge values in each spot,
		and a 0 if no edge exists."""
		max_index = self.find_max_index()
		adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
		for edg in self.edges:
			from_index, to_index = edg.node_from.value, edg.node_to.value
			adjacency_matrix[from_index][to_index] = edg.value
		return adjacency_matrix

	def find_max_index(self):
		"""Return the highest found node number
		Or the length of the node names if set with set_node_names()."""
		if len(self.node_names) > 0:
			return len(self.node_names)
		max_index = -1
		if len(self.nodes):
			for node in self.nodes:
				if node.value > max_index:
					max_index = node.value
		return max_index

	def find_node(self, node_number):
		"Return the node with value node_number or None"
		return self._node_map.get(node_number)
	
	def _clear_visited(self):
		for node in self.nodes:
			node.visited = False

	def dfs_helper(self, start_node):
		"""TODO: Write the helper function for a recursive implementation
		of Depth First Search iterating through a node's edges. The
		output should be a list of numbers corresponding to the
		values of the traversed nodes.
		ARGUMENTS: start_node is the starting Node
		MODIFIES: the value of the visited property of nodes in self.nodes 
		RETURN: a list of the traversed node values (integers).
		"""
		ret_list = [start_node.value]
		start_node.visited = True
		for edge in start_node.edges:
			out_node = edge.node_to
			if not out_node.visited:
				ret_list += self.dfs_helper(out_node)
		return ret_list

	def dfs(self, start_node_num):
		"""Outputs a list of numbers corresponding to the traversed nodes
		in a Depth First Search.
		ARGUMENTS: start_node_num is the starting node number (integer)
		MODIFIES: the value of the visited property of nodes in self.nodes
		RETURN: a list of the node values (integers)."""
		self._clear_visited()
		start_node = self.find_node(start_node_num)
		return self.dfs_helper(start_node)

	def dfs_names(self, start_node_num):
		"""Return the results of dfs with numbers converted to names."""
		return [self.node_names[num] for num in self.dfs(start_node_num)]

	def bfs(self, start_node_num):
		"""TODO: Create an iterative implementation of Breadth First Search
		iterating through a node's edges. The output should be a list of
		numbers corresponding to the traversed nodes.
		ARGUMENTS: start_node_num is the node number (integer)
		MODIFIES: the value of the visited property of nodes in self.nodes
		RETURN: a list of the node values (integers)."""
		node = self.find_node(start_node_num)
		self._clear_visited()
		ret_list = [node.value]
		# Nodes to visit
		queue = [node]
		node.visited = True
		while queue:
			for edge in node.edges:
				node_to = edge.node_to
				if not node_to.visited:
					ret_list.append(node_to.value)
					queue.insert(0, node_to)
					node_to.visited = True
			node = queue.pop()
		return ret_list

	def bfs_names(self, start_node_num):
		"""Return the results of bfs with numbers converted to names."""
		return [self.node_names[num] for num in self.bfs(start_node_num)]

	def _clear_distance_and_from_node(self):
		for node in self.nodes:
			node.distance = float('Inf')
			node.node_from = None

	def _min_unvisited_distance(self):
		"""Finds unvisited node with minimum distance.
		Not an efficient implementation.
		Returns None if no node with distance less than infinity."""
		min_dist = float('Inf')
		min_dist_node = None
		for node in self.nodes:
			if node.distance < min_dist and not node.visited:
				min_dist = node.distance
				min_dist_node = node
		return min_dist_node

	def dijkstra_path(self, dest_node):
		""" Calculates min distance path after running dijkstra algo."""
		# Originating node does not have node_from
		path = []
		while dest_node:
			path += [self.node_names[dest_node.value]]
			dest_node = dest_node.node_from
		path.reverse()
		return path

	def dijkstra(self, start_node_num, find_node_num):
		"""Uses Dijkstra's algorithm to find minimum distance path between nodes.
		ARGUMENTS: 
		  start_node_num is the node number (integer)
		  find_node_num is the distination (integer)
		MODIFIES: the value of the distance property of nodes in self.nodes
		RETURN: a list of the node values (integers)."""
		self._clear_distance_and_from_node()
		self._clear_visited()
		node = self.find_node(start_node_num)
		dest_node = self.find_node(find_node_num)
		# Start node has distance of zero
		node.distance = 0
		while node is not None and not dest_node.visited:
			for edge in node.edges:
				node_to = edge.node_to
				if node_to.visited:
					continue
				# Full path distance from current node
				dist = edge.value + node.distance
				# If distance less than previous shortest path, update min dist and
				# originating node
				if dist < node_to.distance:
					node_to.distance = dist
					node_to.node_from = node
			node.visited = True
			# Next node to visited---unless all unvisited still at infinite distance
			node = self._min_unvisited_distance()
		if dest_node.visited:
			return dest_node.distance, self.dijkstra_path(dest_node)
		return float('Inf'), []


