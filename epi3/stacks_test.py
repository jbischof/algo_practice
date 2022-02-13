import unittest
import stacks
from stacks import Building

class TestStacks(unittest.TestCase):
    def test_stack_with_max(self):
        s = stacks.StackWithMax()
        s.push(1)
        s.push(11)
        s.push(5)
        s.push(25)
        self.assertEqual(s.max(), 25)
        self.assertEqual(s.pop(), 25)
        self.assertEqual(s.max(), 11)
        self.assertEqual(s.pop(), 5)

    def test_sunset_view(self):

        buildings = [
            Building('a', 6),
            Building('b', 3),
            Building('c', 9),
            Building('d', 2),
            Building('e', 6),
            Building('f', 0),
            Building('g', 8),
            Building('h', 2),
            Building('i', 1)
        ]
        self.assertListEqual([x.name for x in stacks.sunset_view(buildings)],
                             ['i', 'h', 'g', 'c'])
        buildings = [
            Building('a', 6),
            Building('b', 3),
            Building('c', 9),
            Building('d', 2),
            Building('e', 6),
            Building('f', 0),
            Building('g', 8),
            Building('h', 2),
            Building('i', 1)
        ]
        self.assertListEqual(
                [x.name for x in stacks.sunset_view_stream(buildings)],
                ['c', 'g', 'h', 'i'])


class TestPostingList(unittest.TestCase):
    def setUp(self):
        self.n1 = stacks.PostingNode()
        self.n2 = stacks.PostingNode()
        self.n3 = stacks.PostingNode()
        self.n4 = stacks.PostingNode()
        self.n5 = stacks.PostingNode()
        self.n1.jump = self.n3
        self.n1.next = self.n2
        self.n2.jump = self.n4
        self.n2.next = self.n3
        self.n3.jump = self.n2
        self.n3.next = self.n4
        self.n4.jump = self.n4
        self.n4.next = self.n5

    def tearDown(self):
        self.n1.order = None
        self.n2.order = None
        self.n3.order = None
        self.n4.order = None
        self.n5.order = None

    def test_traverse_posting_list(self):
        stacks.traverse_posting_list(self.n1) 
        self.assertListEqual(
            [self.n1.order, self.n2.order, self.n3.order, self.n4.order, 
                self.n5.order],
            [0, 2, 1, 3, 4]
        )

    def test_traverse_posting_list_iter(self):
        stacks.traverse_posting_list_iter(self.n1) 
        self.assertListEqual(
            [self.n1.order, self.n2.order, self.n3.order, self.n4.order, 
                self.n5.order],
            [0, 2, 1, 3, 4]
        )



