import unittest
import recursion
from recursion import Node

class TestRecursion(unittest.TestCase):
    def test_gen_permutations(self):
        a = [1, 2, 3]
        perms = [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
        ]
        self.assertCountEqual(
                recursion.gen_permutations(a),
                perms
        )

    def test_tree_diameter(self):
        a = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')
        e = Node('E')
        f = Node('F')
        g = Node('G')
        h = Node('H')
        i = Node('I')
        j = Node('J')
        a.left = b
        b.left = d
        b.right = e
        e.left = f
        f.right = g
        a.right = c
        c.left = h
        c.right = i
        i.right = j
        self.assertEqual(recursion.tree_diameter(a)[1], 8)
        # Now let's make a longest path not using the root
        k = Node('K')
        l = Node('L')
        m = Node('M')
        n = Node('N')
        o = Node('O')
        p = Node('P')
        d.left = k
        k.left = l
        l.left = m
        m.left = n
        g.right = o
        o.right = p
        self.assertEqual(recursion.tree_diameter(a)[1], 11)
