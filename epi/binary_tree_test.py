import unittest
import binary_tree as bt

class BinaryTreeTest(unittest.TestCase):
  def ExampleTree(self):
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
    tree = bt.BinaryTree(a)
    a.left = b
    b.left = c
    c.left = d
    c.right = e
    b.right = f
    f.right = g
    g.left = h
    a.right = i
    i.left = j
    j.right = k
    k.left = l
    l.right = m
    k.right = n
    i.right = o
    o.right = p
    return tree

  def testPreorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.preorder(), 
      [314, 6, 271, 28, 0, 561, 3, 17, 6, 2, 1, 401, 641, 257, 271, 28])

  def testInorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.inorder(), 
      [28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 6, 271, 28])

  def testPostorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.postorder(), 
      [28, 0, 271, 17, 3, 561, 6, 641, 401, 257, 1, 2, 28, 271, 6, 314])

  def testLevelPrint(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.level_print(),
      [[314], [6, 6], [271, 561, 2, 271], [28, 0, 3, 1, 28], [17, 401, 257], 
      [641]])

  def testHeightBal(self):
    a = bt.Node('a')
    b = bt.Node('b')
    c = bt.Node('c')
    d = bt.Node('d')
    e = bt.Node('e')
    f = bt.Node('f')
    g = bt.Node('g')
    tree = bt.BinaryTree(a)
    a.left = b
    b.left = c
    b.right = d
    d.right = e
    a.right = f
    f.right = g
    # Tree is originally height-balanced
    self.assertTrue(tree.is_height_balanced())
    # Without node 'g', no longer true
    f.right = None
    self.assertFalse(tree.is_height_balanced())

