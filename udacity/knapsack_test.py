import unittest
import knapsack

class TestKnapSack(unittest.TestCase):
	def ExampleItems(self):
		return [knapsack.Item(2, 6), knapsack.Item(5, 9), knapsack.Item(4, 5)]

	# If binary knapsack, best to take 1st and 3rd items
	def testBinaryKnapsack(self):
		self.assertEqual(knapsack.binary_knapsack(self.ExampleItems(), 6), 11)

	# If unbounded knapsack, take 3 copies of 1st item
	def testKnapsack(self):
		self.assertEqual(knapsack.knapsack(self.ExampleItems(), 6), 18)

	# If items too big for sack, expect zero
	def testBinaryKnapsackTooSmall(self):
		self.assertEqual(knapsack.binary_knapsack(self.ExampleItems(), 1), 0)
	def testKnapsackTooSmall(self):
		self.assertEqual(knapsack.knapsack(self.ExampleItems(), 1), 0)

if __name__ == '__main__':
		unittest.main()