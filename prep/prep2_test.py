import unittest
import prep2
from prep2 import Node, Annotation

class TestPrep2(unittest.TestCase):
    def test_eval_tree_expr(self):
        a = Node('*')
        b = Node('+')
        c = Node(3)
        d = Node(2)
        e = Node(4)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        self.assertEqual(prep2.eval_tree_expr(a), 18)

    def test_interval_annotation(self):
        a = [
                Annotation('X', 0, 4),
                Annotation('Y', 5, 8),
                Annotation('Z', 3, 6)
            ]
        self.assertListEqual(
                prep2.interval_annotation(a), 
                [
                    ['X', 0, 3], 
                    ['XZ', 3, 4], 
                    ['Z', 4, 5], 
                    ['YZ', 5, 6], 
                    ['Y', 6, 8]
                ]
        )
