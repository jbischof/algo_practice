import unittest
import queues

class TestQueues(unittest.TestCase):
  def testInitQueue(self):
    q = queues.ArrayQueue([2, 4, 6, 8, 12])
    self.assertEqual(q.to_list(), [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 5)

  def testDequeueEnqueue(self):
    q = queues.ArrayQueue([2, 4, 6, 8, 12])
    a = []
    for i in range(q.len()):
      a.append(q.dequeue())
    self.assertEqual(a, [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 0)
    self.assertTrue(q.start is None)
    self.assertTrue(q.end is None)
    self.assertTrue(q.dequeue() is None)
    q.enqueue_list([4, 5])
    self.assertEqual(q.to_list()[0:2], [4, 5])
    self.assertEqual(q.len(), 2)
    self.assertTrue(q.start is 0)
    self.assertTrue(q.end is 1)
    self.assertEqual(q.dequeue(), 4)

  def testResize(self):
    q = queues.ArrayQueue([2, 4, 6, 8], 5)
    q.enqueue_list([12, 15])
    self.assertEqual(q.len(), 6)
    self.assertEqual(q.max_size, 10)  

  def testResizeWithDequeue(self):
    q = queues.ArrayQueue([2, 4, 6, 8], 5)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 4)    
    self.assertEqual(q.start, 2)
    self.assertEqual(q.end, 3)
    q.enqueue_list([12, 15, 17, 19])  
    self.assertEqual(q.len(), 6)
    self.assertEqual(q.max_size, 10)
    self.assertEqual(q.start, 0)
    self.assertEqual(q.end, 5)

class TestCircQueues(unittest.TestCase):
  def testInitQueue(self):
    q = queues.CircQueue([2, 4, 6, 8, 12])
    self.assertEqual(q.to_list(), [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 5)

  def testDequeueEnqueue(self):
    q = queues.CircQueue([2, 4, 6, 8, 12])
    a = []
    for i in range(q.len()):
      a.append(q.dequeue())
    self.assertEqual(a, [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 0)
    self.assertTrue(q.dequeue() is None)
    q.enqueue_list([4, 5])
    self.assertEqual(q.to_list()[0:2], [4, 5])
    self.assertEqual(q.len(), 2)
    self.assertTrue(q.start is 0)
    self.assertTrue(q.end is 1)
    self.assertEqual(q.dequeue(), 4)

  def testResize(self):
    q = queues.CircQueue([2, 4, 6, 8], 5)
    q.enqueue_list([12, 15])
    self.assertEqual(q.len(), 6)
    self.assertEqual(q.max_size, 10)  

  def testResizeWithDequeue(self):
    q = queues.CircQueue([2, 4, 6, 8], 5)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 4)    
    self.assertEqual(q.start, 2)
    self.assertEqual(q.end, 3)
    q.enqueue_list([12, 15, 17, 19])  
    self.assertEqual(q.len(), 6)
    self.assertEqual(q.max_size, 10)
    self.assertEqual(q.start, 0)
    self.assertEqual(q.end, 5)

  def testCircWrite(self):
    q = queues.CircQueue([2, 4, 6, 8, 12, 15, 17, 18], 10)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 4)
    q.enqueue_list([19, 20, 25, 27])
    self.assertEqual(q.queue, [25, 27, 6, 8, 12, 15, 17, 18, 19, 20])
    self.assertEqual(q.start, 2)
    self.assertEqual(q.end, 1)
    q.enqueue(29)
    self.assertEqual(q.len(), 11)
    self.assertEqual(q.queue[0:11], [6, 8, 12, 15, 17, 18, 19, 20, 25, 27, 29])
    
class TestTwoStackQueues(unittest.TestCase):
  def testInitQueue(self):
    q = queues.TwoStackQueue([2, 4, 6, 8, 12])
    self.assertEqual(q.to_list(), [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 5)

  def testDequeueEnqueue(self):
    q = queues.TwoStackQueue([2, 4, 6, 8, 12])
    a = []
    for i in range(q.len()):
      a.append(q.dequeue())
    self.assertEqual(a, [2, 4, 6, 8, 12])
    self.assertEqual(q.len(), 0)
    self.assertTrue(q.dequeue() is None)
    q.enqueue_list([4, 5])
    self.assertEqual(q.to_list(), [4, 5])
    self.assertEqual(q.len(), 2)
    self.assertEqual(q.dequeue(), 4)
    q.enqueue_list([6, 7])
    self.assertEqual(q.dequeue(), 5)
    self.assertEqual(q.dequeue(), 6)
