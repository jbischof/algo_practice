import stack_queue as sq
import unittest

class TestStackQueue(unittest.TestCase):
  def testStackWithMin(self):
    stack = sq.StackWithMin()
    self.assertTrue(stack.isEmpty())
    self.assertEqual(stack.peek(), None)
    self.assertEqual(stack.min(), None)
    self.assertEqual(stack.pop(), None)
    stack.push(3)
    stack.push(11)
    stack.push(1)
    stack.push(7)
    self.assertEqual(stack.peek(), 7)
    self.assertEqual(stack.min(), 1)
    self.assertEqual(stack.pop(), 7)
    self.assertEqual(stack.min(), 1)
    self.assertEqual(stack.pop(), 1)
    self.assertEqual(stack.min(), 3)

  def testQueueFromStack(self): 
    queue = sq.QueueFromStack()
    self.assertEqual(queue.pop(), None)
    self.assertEqual(queue.peek(), None)
    queue.push(3)
    queue.push(0)
    queue.push(4)
    queue.push(1)
    self.assertEqual(queue.peek(), 3)
    self.assertEqual(queue.pop(), 3)
    self.assertEqual(queue.pop(), 0)
    queue.push(10)
    queue.push(7)
    self.assertEqual(queue.pop(), 4)
    self.assertEqual(queue.pop(), 1)
    self.assertEqual(queue.pop(), 10)
    self.assertEqual(queue.pop(), 7)
    self.assertEqual(queue.pop(), None)
