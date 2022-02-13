import queues
import unittest

class TestQueues(unittest.TestCase):
    def test_queue_with_max(self):
        q = queues.QueueWithMax()
        q.push(4)
        self.assertEqual(q.max(), 4)
        q.push(8)
        self.assertEqual(q.max(), 8)
        q.extend([5, 2, 7, 2, 1, 4])
        self.assertEqual(q.max(), 8)
        self.assertEqual(q.pop(), 4)
        self.assertEqual(q.pop(), 8)
        self.assertEqual(q.max(), 7)
        
