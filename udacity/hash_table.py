"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
	def __init__(self):
		self.table = [None]*10000

	def store(self, string):
		"""Input a string that's stored in 
		the table."""
		idx = self.calculate_hash_value(string)
		if idx < 0:
			return -1
		if self.table[idx]:
			self.table[idx].append(string)
		else:
			self.table[idx] = [string]
		return 0

	def lookup(self, string):
		"""Return the hash value if the
		string is already in the table.
		Return -1 otherwise."""
		idx = self.calculate_hash_value(string)
		xlist = self.table[idx]		
		if not xlist:
			return -1
		for val in xlist:
			if val == string:
				return idx
		return -1

	def calculate_hash_value(self, string):
		"""Helper function to calulate a
		hash value from a string."""
		if not string:
			return -1
		if len(string) < 2:
			return ord(string[0]) * 100
		return ord(string[0]) * 100 + ord(string[1])
