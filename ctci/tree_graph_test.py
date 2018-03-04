"""Tests for tree and graph problems."""

import tree_graph as tg
import unittest

class TreeGraphTest(unittest.TestCase):
  def ExampleTree(self):
    """An example tree with parent connections."""
    a = tg.Node(314)
    b = tg.Node(6)
    c = tg.Node(271)
    d = tg.Node(28)
    e = tg.Node(0)
    f = tg.Node(561)
    g = tg.Node(3)
    h = tg.Node(17)
    i = tg.Node(6)
    j = tg.Node(2)
    k = tg.Node(1)
    l = tg.Node(401)
    m = tg.Node(641)
    n = tg.Node(257)
    o = tg.Node(271)
    p = tg.Node(28)
    tree = tg.Tree(a)
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
    return tree

  def testIsConnected(self):
    graph = tg.Graph({
      'a': ['b', 'e'],
      'b': ['a', 'c', 'd'],
      'c': ['b', 'd'],
      'd': ['b', 'c'],
      'e': ['a'],
      'g': ['f', 'h'],
      'f': ['g', 'h'],
      'h': ['f', 'g']})
    self.assertTrue(graph.isConnected('a', 'c'))
    self.assertFalse(graph.isConnected('a', 'g'))
    self.assertTrue(graph.isConnected('g', 'h'))

  def testFromSortedList(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    tree = tg.Tree.from_sorted_list(a)
    self.assertEqual(tree.root.value, 5)
    self.assertEqual(tree.root.left.value, 3)
    self.assertEqual(tree.root.right.value, 15)
    self.assertEqual(tree.root.left.left.value, 0)
    self.assertEqual(tree.root.left.right.value, 4)
    self.assertEqual(tree.root.right.left.value, 11)
    self.assertEqual(tree.root.right.right.value, 17)

  def testInorder(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    tree = tg.Tree.from_sorted_list(a)
    self.assertEqual(tree.inorder(), a)

  def testLevelLists(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    tree = tg.Tree.from_sorted_list(a)
    self.assertEqual(tree.level_lists(), [[5], [3, 15], [0, 4, 11, 17]])

  def testIsBalanced(self):
    a = tg.Node('a')
    b = tg.Node('b')
    c = tg.Node('c')
    d = tg.Node('d')
    e = tg.Node('e')
    f = tg.Node('f')
    g = tg.Node('g')
    tree = tg.Tree(a)
    a.left = b
    b.left = c
    b.right = d
    d.right = e
    a.right = f
    f.right = g
    # Tree is originally balanced
    self.assertTrue(tree.is_balanced())
    # Without node 'g', no longer true
    f.right = None
    self.assertFalse(tree.is_balanced())

  def testIsBST(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    tree = tg.Tree.from_sorted_list(a)
    self.assertTrue(tree.is_bst())
    tree.root.left.right.value = 6
    self.assertFalse(tree.is_bst())
      
  def testInorderSuccessor(self):
    a = tg.Node('a')
    b = tg.Node('b')
    c = tg.Node('c')
    d = tg.Node('d')
    e = tg.Node('e')
    f = tg.Node('f')
    g = tg.Node('g')
    tree = tg.Tree(a)
    a.parent = None
    a.left = b
    b.parent = a
    b.left = c
    c.parent = b
    b.right = d
    d.parent = b
    d.right = e
    e.parent = d
    a.right = f
    f.parent = a
    f.right = g
    g.parent = f
    # Has right child
    self.assertEqual(tree.inorder_successor(a), f)
    # No right child but is left child 
    self.assertEqual(tree.inorder_successor(c), b)
    # Biggest node in subtree 
    self.assertEqual(tree.inorder_successor(e), a)
    # Biggest node in tree 
    self.assertEqual(tree.inorder_successor(g), None)

  def testBuildOrder(self):
    jobs = ['a', 'b', 'c', 'd', 'e', 'f']
    depend_pairs = [('a', 'd'),
                    ('f', 'b'),
                    ('b', 'd'),
                    ('f', 'a'),
                    ('d', 'c')]
    self.assertTrue(tg.build_order(jobs, depend_pairs))
    # Create a cycle
    depend_pairs.append(('c', 'a'))
    self.assertFalse(tg.build_order(jobs, depend_pairs))

  def testTreeEquality(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    tree1 = tg.Tree.from_sorted_list(a)
    tree2 = tg.Tree.from_sorted_list(a)
    self.assertTrue(tree1 == tree2)
    self.assertFalse(tree1 != tree2)
    tree1.root.left.left = None
    self.assertFalse(tree1 == tree2)
    self.assertTrue(tree1 != tree2)
    tree1 = tg.Tree.from_sorted_list(a)
    tree1.root.right.value = 14
    self.assertFalse(tree1 == tree2)
    self.assertTrue(tree1 != tree2)

  def testHasSubtree(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    b = [0, 3, 4]
    c = [1, 3, 4]
    tree1 = tg.Tree.from_sorted_list(a)
    tree2 = tg.Tree.from_sorted_list(b)
    tree3 = tg.Tree.from_sorted_list(b)
    tree4 = tg.Tree.from_sorted_list(c)
    # Normal subtree
    self.assertTrue(tree1.has_subtree(tree2))
    # Subtree is entire tree
    self.assertTrue(tree2.has_subtree(tree3))
    # Not subtree
    self.assertFalse(tree1.has_subtree(tree4))
