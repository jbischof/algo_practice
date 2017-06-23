class Node():
	def __init__(self, value=0):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self, head=None):
		self.head = head
		self.tail = head

	@classmethod
	def from_list(cls, input_list):
		""" Instantiate linked list from regular list. """
		llist = cls()
		for value in input_list:
			llist.insert_at_tail(Node(value))
		return llist

	def to_list(self):
		""" Return linked list as regular list. O(N) operation. """
		ret = []
		next_node = self.head
		while next_node:
			ret.append(next_node.value)
			next_node = next_node.next
		return ret

	def search(self, value):
		next_node = self.head
		while next_node:
			if next_node.value == value:
				return next_node
			next_node = next_node.next
		return None

	def insert_at_tail(self, new_node):
		# Make node the head if list empty
		if not self.head:
			self.head = new_node
			self.tail = new_node
			return
		self.tail.next = new_node
		self.tail = new_node

	def insert_at_head(self, new_node):
		if self.head:
			new_node.next = self.head
		self.head = new_node
		# Update tail if this the only node
		if not self.head.next:
			self.tail = self.head

	def insert_after(self, node, new_node):
		new_node.next = node.next
		node.next = new_node
		# Update tail if inserted at end
		if not new_node.next:
			self.tail = new_node

	def delete_after(self, node):
		if node.next:
			node.next = node.next.next
		if not node.next:
			self.tail = node

	def traverse(self, k, node=None):
		""" Return node 'k' steps from the start node. Returns None if moves past
		tail of list. """
		if not node:
			node = self.head
		for i in range(k):
			if node:
				node = node.next
		return node

	def pop(self):
		""" Remove and return head from list """
		ret = None
		if self.head:
			ret = self.head
			self.head = self.head.next
			ret.next = None
		return ret

	def reverse_subset(self, i, j):
		""" Reverse order of a subset of LL delimited by i to j """
		# Insert dummy node if i = 0 for logic to work
		self.insert_at_head(Node(0))
		i += 1
		j += 1
		next_move_before = self.traverse(i - 1)
		next_move = self.traverse(1, next_move_before)
		move_after = self.traverse(j - i, next_move)
		for l in range(j-i):
			self.delete_after(next_move_before)
			self.insert_after(move_after, next_move)
			next_move = next_move_before.next
		self.pop()

	def check_cycles(self):
		""" Checks for cycles in list and returns whether cycle present and location
		of iterater collison"""
		# Create two iterators, one fast and one slow
		# Know there is a cycle if converge on same node
		it1 = self.head
		it2 = self.traverse(2)
		loc = None
		has_cycle = False
		while it1 and it2:
			if it1 is it2:
				has_cycle = True
				loc = it1
				break
			it1 = it1.next
			it2 = self.traverse(2, it2)
		return has_cycle, loc

	def find_cycle(self):
		""" Checks for cycles in list and returns location of cycle start if present
		"""
		has_cycle, loc = self.check_cycles()
		if not has_cycle:
			return None
		# Step 1: calculate length of cycle
		it = loc.next
		cyc_len = 1
		while it is not loc:
			cyc_len += 1
			it = it.next
		# Step 2: figure out length of non-cycle section
		# start two iterators 'cyc_len' apart
		it1 = self.head
		it2 = self.traverse(cyc_len)
		start_len = 0
		while it1 != it2:
			start_len += 1
			it1 = it1.next
			it2 = it2.next
		return self.traverse(start_len)

def merge_sorted_linked_list_clumsy(l1, l2):
	""" Merges two sorted linked lists without allocating new memory """
	# If first list is empty, return the other one
	if l1.head is None:
		return l2
	# If second list empty but not the first, return the first
	elif l2.head is None:
		return l1
	# Now know both lists have values. Merge into smaller list since hard to
	# insert left. All merges should be to the right now.
	if l1.head.value < l2.head.value:
		small, big = l1, l2
	else:
		small, big = l2, l1
	small_node, small_node_next, big_node = small.head, small.head.next, big.head
	while big_node:
		big_node_next = big_node.next
		# Case 1: At end of small list: just insert big_node at tail
		if small_node_next is None:
			small.insert_after(small_node, big_node)
			small_node = big_node
			big_node = big_node_next
		# Case 2: big_node belongs between small_node and small_node_next
		elif big_node.value <= small_node_next.value:
			small.insert_after(small_node, big_node)
			small_node = big_node
			small_node_next = big_node.next
			big_node = big_node_next
		# Case 3: big_node belongs somewhere after small_node_next
		elif big_node.value > small_node_next.value:
			small_node = small_node_next
			small_node_next = small_node_next.next
	return small

def merge_sorted_linked_list(l1, l2):
	""" Merges two sorted linked lists without allocating new memory
	Cleverness lesson: don't be afraid to make new container since won't use
	more space """
	# Create dummy head to hold final result
	dummy = Node(0)
	next_node = dummy

	while l1.head and l2.head:
		if l1.head.value <= l2.head.value:
			next_node.next = l1.pop()
		else:
			next_node.next = l2.pop()
		next_node = next_node.next

	# Append rest of remaining list:
	if l1.head:
		next_node.next = l1.head
	else:
		next_node.next = l2.head
	return LinkedList(dummy.next)





