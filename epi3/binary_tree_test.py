
import unittest
import binary_tree as bt

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.a = bt.Node(314)
        self.b = bt.Node(6)
        self.c = bt.Node(271)
        self.d = bt.Node(28)
        self.e = bt.Node(0)
        self.f = bt.Node(561)
        self.g = bt.Node(3)
        self.h = bt.Node(17)
        self.i = bt.Node(6)
        self.j = bt.Node(2)
        self.k = bt.Node(1)
        self.l = bt.Node(401)
        self.m = bt.Node(641)
        self.n = bt.Node(257)
        self.o = bt.Node(271)
        self.p = bt.Node(28)
        self.a.left = self.b
        self.b.left = self.c
        self.c.left = self.d
        self.c.right = self.e
        self.b.right = self.f
        self.f.right = self.g
        self.g.left = self.h
        self.a.right = self.i
        self.i.left = self.j
        self.j.right = self.k
        self.k.left = self.l
        self.l.right = self.m
        self.k.right = self.n
        self.i.right = self.o
        self.o.right = self.p
        self.b.parent = self.a
        self.c.parent = self.b
        self.d.parent = self.c
        self.e.parent = self.c
        self.f.parent = self.b
        self.g.parent = self.f
        self.h.parent = self.g
        self.i.parent = self.a
        self.j.parent = self.i
        self.k.parent = self.j
        self.l.parent = self.k
        self.m.parent = self.l
        self.n.parent = self.k
        self.o.parent = self.i
        self.p.parent = self.o
        self.tree = self.a 

        # Simple tree
        #       1
        #     /   \
        #    2     3
        #   / \
        #  4   5
        #       \
        #        6
        self.one = bt.Node(1)
        self.two = bt.Node(2)
        self.three = bt.Node(3)
        self.four = bt.Node(4)
        self.five = bt.Node(5)
        self.six = bt.Node(6)
        self.two.parent = self.one
        self.three.parent = self.one
        self.four.parent = self.two
        self.five.parent = self.two
        self.six.parent = self.five
        self.one.left = self.two
        self.two.left = self.four
        self.two.right = self.five
        self.five.right = self.six
        self.one.right = self.three
        self.simple_tree = self.one

    def test_is_tree_balanced(self):
        self.assertFalse(bt.is_tree_balanced(self.tree)[1])
        self.assertFalse(bt.is_tree_balanced(self.simple_tree)[1])
        # Tree is balanced if node six removed
        self.five.right = None
        self.assertTrue(bt.is_tree_balanced(self.simple_tree)[1])

    def test_least_common_ancestor(self):
        self.assertEqual(
                bt.least_common_ancestor(
                    self.simple_tree, self.four, self.six)[2],
                self.two
        )
        self.assertEqual(
                bt.least_common_ancestor(
                    self.simple_tree, self.three, self.six)[2],
                self.one
        )

    def test_sort_nodes_by_level(self):
        self.assertListEqual(
                bt.sort_nodes_by_level(self.simple_tree),
                [[1], [2, 3], [4, 5], [6]]
        )

    def test_inorder_traversal_stack(self):
        self.assertListEqual(
                bt.inorder_traversal_stack(self.simple_tree), 
                [4, 2, 5, 6, 1, 3]
        )

    def test_compute_successor(self):
        """
              1
            /   \
           2     3
          / \
         4   5
              \
               6
        """
        self.assertEqual(bt.compute_successor(self.one), self.three)
        self.assertEqual(bt.compute_successor(self.two), self.five)
        self.assertIsNone(bt.compute_successor(self.three))
        self.assertEqual(bt.compute_successor(self.four), self.two)
        self.assertEqual(bt.compute_successor(self.five), self.six)
        self.assertEqual(bt.compute_successor(self.six), self.one)
        # Need bigger tree to check non-trivial right subtree
        self.assertEqual(bt.compute_successor(self.a), self.j)

        self.assertEqual(bt.compute_successor_nr(self.one), self.three)
        self.assertEqual(bt.compute_successor_nr(self.two), self.five)
        self.assertIsNone(bt.compute_successor_nr(self.three))
        self.assertEqual(bt.compute_successor_nr(self.four), self.two)
        self.assertEqual(bt.compute_successor_nr(self.five), self.six)
        self.assertEqual(bt.compute_successor_nr(self.six), self.one)
        # Need bigger tree to check non-trivial right subtree
        self.assertEqual(bt.compute_successor_nr(self.a), self.j)
