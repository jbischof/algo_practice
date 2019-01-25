import unittest
import stack_queue as sq

class StackQueueTest(unittest.TestCase):
  def testRPN(self):
    self.assertEqual(sq.rpn('15,7,1,1,+,-,/,3,*,2,1,1,+,+,-'), 5)
    self.assertRaises(ValueError, sq.rpn, '15,7,1,+,-,/,3,*,2,1,1,+,+,-')

  def testValidParens(self):
    self.assertTrue(sq.valid_parens('[(a+b) * c] / d'))
    # Open paren unmatched
    self.assertFalse(sq.valid_parens('[(a+b) * c / d'))
    # Close paren unmatched
    self.assertFalse(sq.valid_parens('[a+b) * c] / d'))

  def testNormalizePath(self):
    # Normal abs path
    self.assertEqual(sq.normalize_path('/usr/lib/../bin/gcc/'),
                     '/usr/bin/gcc')
    # Normal (if convoluted) rel path
    self.assertEqual(
        sq.normalize_path('scripts//./../scripts/awkscripts/././'),
        'scripts/awkscripts')
    # Path with net positive parent pointers
    self.assertEqual(sq.normalize_path('lib/../../../'), '../..')
    # Absolute path with net positive parent points (invalid)
    self.assertRaises(ValueError, sq.normalize_path, '/usr/lib/../../../')
    # Path with invalid characters
    self.assertRaisesRegexp(ValueError, 'Invalid character \? in path.',
        sq.normalize_path, '/usr/lib/?/gcc/')

  def testQueueWithMax(self):
    q = sq.QueueWithMax()
    q.enqueue_multiple([5, 22, 3, 7, 11, 1, 10])
    self.assertEqual(q.max(), 22)
    self.assertEqual(q.dequeue(), 5)    
    self.assertEqual(q.dequeue(), 22)    
    self.assertEqual(q.max(), 11)
