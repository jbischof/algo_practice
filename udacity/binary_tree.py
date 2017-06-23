class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def search(self, find_val):
		"""Return True if the value is in the tree, return False otherwise."""
		return self.preorder_search(self.root, find_val)

	def print_tree(self):
		"""Print out all tree nodes as they are visited in a pre-order 
		traversal."""
		return self.preorder_print(self.root, "")

	def preorder_search(self, start, find_val):
		"""Explore children of one node."""
		if start.value == find_val:
			return True
		if start.left:
			return self.preorder_search(start.left, find_val)
		if start.right:
			return self.preorder_search(start.right, find_val)		
		return False

	def preorder_print(self, start, traversal):
		"""Helper method - use this to create a recursive print solution."""
		if start.value:
			if traversal:
				traversal = traversal + "-" + str(start.value)
			else:
				traversal = str(start.value)
		if start.left:
			traversal = self.preorder_print(start.left, traversal)
		if start.right:
			traversal = self.preorder_print(start.right, traversal)
		return traversal