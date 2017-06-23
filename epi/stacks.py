class Item():
	def __init__(self, value, max):
		self.value = value
		self.max = max

class Stack():
	def __init__(self, input_list=[]):
		self.stack = []
		for value in input_list:
			self.push(value)

	def peek(self):
		if not self.stack:
			return None
		return self.stack[-1].value

	def max(self):
		if not self.stack:
			return None
		return self.stack[-1].max

	def push(self, value):
		max_value = self.max()
		if not max_value or value > max_value:
			max_value = value
		self.stack.append(Item(value, max_value))

	def pop(self):
		if not self.stack:
			return None
		return self.stack.pop().value

	def to_list(self):
		return [x.value for x in self.stack]

def rpn2int(s):
	""" Evaluate reverse Polish notation string to int
	Args:
		s: A comma-separated string with numbers and operators
	Returns:
		int
	"""
	in_list = s.split(',')
	ostack = Stack()
	for val in in_list:
		if val in '+-*/':
			second = ostack.pop()
			first = ostack.pop()
			if val == '+':
				val = first + second
			elif val == '-':
				val = first - second
			elif val == '*':
				val = first * second
			elif val == '/':
				val = first / second
		ostack.push(int(val))
	return ostack.pop()

def checkParen(s):
	""" Checks whether string of parens is valid. Valid strings will close parens
	in the reverse order that they were opened. 
	Args:
		s: A string of parens '(){}[]' 
	Returns:
		Boolean indicating validatity of string
	"""
	openParens = '({['
	closeParens = ')}]'
	matches = {'(':')', '{':'}', '[':']'}
	pstack = Stack()
	for p in s:
		if p in openParens:
			pstack.push(p)
		# If p is a closeParens, top item in stack must be the matching open parens
		# Also, stack cannot be empty
		elif p in closeParens:
			partner = pstack.pop()
			if not partner or matches[partner] != p:
				return False
	# If anything left in stack, have hanging parens
	if pstack.peek():
		return False
	return True


