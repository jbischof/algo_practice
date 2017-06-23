class Item(object):
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value
		self.added = False

def _clear_items(items):
	for item in items:
		item.added = False

def binary_knapsack(items, total_weight):
	""" Solves the knapsack problem for binary inclusion.
	Args:
	  items: An array of Item objects
	  total_weight: the total capacity of the knapsack
	Returns:
		list of items to put in knapsack
	"""

	# Initialize weight/value array
	# Index i is best value for weight i
	vals = [0] * (total_weight + 1)
	_clear_items(items)

	for item in items:
		for weight, val in enumerate(vals):
			extra = weight - item.weight
			if extra < 0:
				continue
			if item.added:
				new_val = vals[weight - 1]
			else:
				new_val = vals[extra] + item.value
			if new_val > val:
				vals[weight] = new_val
				item.added = True
	return max(vals)

def knapsack(items, total_weight):
	""" Solves the knapsack problem for unbounded inclusion.
	Args:
	  items: An array of Item objects
	  total_weight: the total capacity of the knapsack
	Returns:
		list of items to put in knapsack
	"""

	# Initialize weight/value array
	# Index i is best value for weight i
	vals = [0] * (total_weight + 1)
	_clear_items(items)

	for item in items:
		for weight, val in enumerate(vals):
			extra = weight - item.weight
			if extra < 0:
				continue
			new_val = vals[extra] + item.value
			if new_val > val:
				vals[weight] = new_val
	return max(vals)