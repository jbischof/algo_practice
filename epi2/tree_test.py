"""Testing the trees."""
import unittest
import tree as bt

class TreeTest(unittest.TestCase):
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

  def testPreorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.preorder(), 
      [314, 6, 271, 28, 0, 561, 3, 17, 6, 2, 1, 401, 641, 257, 271, 28])

  def testInorder(self):
    tree = self.ExampleTree()
    expect_inorder = [28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 6,
                      271, 28] 
    self.assertEqual(tree.inorder(), expect_inorder)

  def testPostorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.postorder(), 
      [28, 0, 271, 17, 3, 561, 6, 641, 401, 257, 1, 2, 28, 271, 6, 314])

  def testIsHeightBalanced(self):
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

  def testHasPathSum(self):
    tree = self.ExampleTree()
    self.assertTrue(tree.has_path_sum(619))
    self.assertFalse(tree.has_path_sum(618))
    
