import unittest
import binary_tree

class TestBinaryTree(unittest.TestCase):
	def ExampleTree(self):
		tree = binary_tree.BinaryTree(1)
		tree.root.left = binary_tree.Node(2)
		tree.root.right = binary_tree.Node(3)
		tree.root.left.left = binary_tree.Node(4)
		tree.root.left.right = binary_tree.Node(5)
		return tree

	def testSearch(self):
		tree = self.ExampleTree()
		self.assertTrue(tree.search(1))
		self.assertTrue(tree.search(4))
		self.assertFalse(tree.search(6))

	def testPrint(self):
		tree = self.ExampleTree()
		self.assertEqual(tree.print_tree(), '1-2-4-5-3')

if __name__ == '__main__':
		unittest.main()