import unittest
import binary_search_tree

class TestBinarySearchTree(unittest.TestCase):

	def testInsertAndSearch(self):
		tree = binary_search_tree.BST(4)
		tree.insert(2)
		tree.insert(1)
		tree.insert(3)
		tree.insert(5)
		self.assertTrue(tree.search(4))
		self.assertFalse(tree.search(6))

if __name__ == '__main__':
		unittest.main()