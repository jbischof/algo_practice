class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = Node(root)

	def insert(self, new_val):
		return self.preorder_insert(self.root, new_val)

	def search(self, find_val):
		return self.preorder_search(self.root, find_val)

	def preorder_search(self, start, find_val):
		if start.value == find_val:
			return True
		if start.left and start.value > find_val:
			self.preorder_search(start.left, find_val)
		if start.right:
			self.preorder_search(start.right, find_val)
		return False

	def preorder_insert(self, start, new_val):
		# Look to the left if less
		if new_val < start.value:
			if (not start.left) or (new_val > start.left.value):
				new_node = Node(new_val)
				new_node.left = start.left
				start.left = new_node
			if new_val < start.left.value:
				self.preorder_insert(start.left, new_val)
		# Look to the right if more
		if new_val > start.value:
			if (not start.right) or (new_val < start.right.value):
				new_node = Node(new_val)
				new_node.right = start.right
				start.right = new_node
			if new_val > start.right.value:
				self.preorder_insert(start.right, new_val)	
