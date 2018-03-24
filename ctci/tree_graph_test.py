"""Tests for tree and graph problems."""

import tree_graph as tg
import unittest

class TreeGraphTest(unittest.TestCase):
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

  def testBFS(self):
    a = [0, 3, 4, 5, 11, 15, 17]
    expect_bfs = [5, 3, 15, 0, 4, 11, 17]
    tree = tg.Tree.from_sorted_list(a)
    self.assertEqual(tree.bfs(), expect_bfs)

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
