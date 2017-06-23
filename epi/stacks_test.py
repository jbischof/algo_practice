import stacks
import unittest

class TestStacks(unittest.TestCase):
	def testStackPush(self):
		stack = stacks.Stack([5, 8, 3, 12, 2])
		self.assertEqual(stack.to_list(), [5, 8, 3, 12, 2])
		stack.push(4)
		self.assertEqual(stack.to_list(), [5, 8, 3, 12, 2, 4])

	def testStackPeek(self):
		stack = stacks.Stack([5, 8, 3, 12, 2])
		self.assertEqual(stack.peek(), 2)
		self.assertEqual(stack.to_list(), [5, 8, 3, 12, 2])
		stack = stacks.Stack()
		self.assertEqual(stack.peek(), None)

	def testStackPop(self):
		stack = stacks.Stack([5, 8, 3, 12, 2])
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.to_list(), [5, 8, 3, 12])
		stack = stacks.Stack()
		self.assertEqual(stack.peek(), None)		

	def testStackMax(self):
		stack = stacks.Stack([5, 8, 3, 12, 2])
		self.assertEqual(stack.max(), 12)
		stack.pop()
		stack.pop()
		self.assertEqual(stack.max(), 8)		
		stack.push(15)
		self.assertEqual(stack.max(), 15)		
		stack = stacks.Stack()
		self.assertEqual(stack.max(), None)			

	def testRPN2Int(self):
		self.assertEqual(stacks.rpn2int('-4'), -4)
		self.assertEqual(stacks.rpn2int('-4,3,+'), -1)
		self.assertEqual(stacks.rpn2int('-4,3,+,6,*'), -6)
		self.assertEqual(stacks.rpn2int('-4,3,+,6,*,-3,/'), 2)

	def testCheckParen(self):
		self.assertTrue(stacks.checkParen('()'))
		self.assertTrue(stacks.checkParen('([]){()}'))
		self.assertTrue(stacks.checkParen('[()[]{()()}]'))
		self.assertFalse(stacks.checkParen('{)'))
		self.assertFalse(stacks.checkParen('[()[]{()()'))

