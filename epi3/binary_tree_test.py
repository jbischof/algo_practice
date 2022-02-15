
import unittest
import binary_tree as bt

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        a = bt.Node(314)
        b = bt.Node(6)
        c = bt.Node(271)
        d = bt.Node(28)
        e = bt.Node(0)
        f = bt.Node(561)
        g = bt.Node(3)
        h = bt.Node(17)
        i = bt.Node(6)
        j = bt.Node(2)
        k = bt.Node(1)
        l = bt.Node(401)
        m = bt.Node(641)
        n = bt.Node(257)
        o = bt.Node(271)
        p = bt.Node(28)
        a.left = b
        b.parent = a
        b.left = c
        c.parent = b
        c.left = d
        d.parent = c
        c.right = e
        e.parent = c
        b.right = f
        f.parent = b
        f.right = g
        g.parent = f
        g.left = h
        h.parent = g
        a.right = i
        i.parent = a
        i.left = j
        j.parent = i
        j.right = k
        k.parent = j
        k.left = l
        l.parent = k
        l.right = m
        m.parent = l
        k.right = n
        n.parent = k
        i.right = o
        o.parent = i
        o.right = p
        p.parent = o
        self.tree = a 

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
   

