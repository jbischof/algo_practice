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
    self.assertEqual(tree.inorder_no_recursion(), expect_inorder)
    self.assertEqual(tree.inorder_no_space(), expect_inorder)

  def testPostorder(self):
    tree = self.ExampleTree()
    self.assertEqual(
      tree.postorder(), 
      [28, 0, 271, 17, 3, 561, 6, 641, 401, 257, 1, 2, 28, 271, 6, 314])

  def testPreOrderInOrderBaseCase(self):
    a = bt.Node('a')
    b = bt.Node('b')
    c = bt.Node('c')
    # First case: fully connected
    a.left = b
    a.right = c
    preorder = ['a', 'b', 'c']
    postorder = ['b', 'a', 'c']
    ans = bt.BinaryTree.preorder_inorder_base_case(preorder, postorder)
    self.assertEqual(bt.BinaryTree(a), bt.BinaryTree(ans)) 
    # Second case: only left
    a.left = b
    a.right = None
    preorder = ['a', 'b']
    postorder = ['b', 'a']
    ans = bt.BinaryTree.preorder_inorder_base_case(preorder, postorder)
    self.assertEqual(bt.BinaryTree(a), bt.BinaryTree(ans)) 
    # Third case: only right
    a.left = None
    a.right = c
    preorder = ['a', 'c']
    postorder = ['a', 'c']
    ans = bt.BinaryTree.preorder_inorder_base_case(preorder, postorder)
    self.assertEqual(bt.BinaryTree(a), bt.BinaryTree(ans)) 
    # Fourth case: no children
    a.left = None
    a.right = None
    preorder = ['a']
    postorder = ['a']
    ans = bt.BinaryTree.preorder_inorder_base_case(preorder, postorder)
    self.assertEqual(bt.BinaryTree(a), bt.BinaryTree(ans)) 

  def testPreOrderInOrder(self):
    tree = self.ExampleTree()
    inorder = [28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 6, 271, 28]
    preorder = [314, 6, 271, 28, 0, 561, 3, 17, 6, 2, 1, 401, 641, 257, 271, 28]
    ans = bt.BinaryTree.from_preorder_inorder(preorder, inorder)
    self.assertEqual(tree, ans) 

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

  def testIsSymmetric(self):
    a = bt.Node(1)
    b = bt.Node(2)
    c = bt.Node(3)
    d = bt.Node(4)
    e = bt.Node(2)
    f = bt.Node(4)
    g = bt.Node(3)
    tree = bt.BinaryTree(a)
    a.left = b
    b.left = c
    b.right = d
    a.right = e
    e.left = f
    e.right = g
    # Tree is originally symmetric
    self.assertTrue(tree.is_symmetric())
    # If value of node 'g' changes, not true
    g.value = -1
    self.assertFalse(tree.is_symmetric())
    # Without node 'g', no longer true
    e.right = None
    self.assertFalse(tree.is_symmetric())

  def testLeastCommonAncestor(self):
    a = bt.Node('a')
    b = bt.Node('b')
    c = bt.Node('c')
    d = bt.Node('d')
    e = bt.Node('e')
    f = bt.Node('f')
    g = bt.Node('g')
    h = bt.Node('h')
    i = bt.Node('i')
    tree = bt.BinaryTree(a)
    a.left = b
    b.parent = a
    b.left = c
    c.parent = b
    b.right = d
    d.parent = b
    c.left = e
    e.parent = c
    a.right = f
    f.parent = a
    f.left = g
    g.parent = f
    f.right = h
    h.parent = f
    h.right = i
    i.parent = h
    self.assertEqual(tree.get_ancestry(i), [h, f, a])
    self.assertEqual(tree.get_ancestry(a), [])
    self.assertEqual(tree.least_common_ancestor(e, d), b)
    self.assertEqual(tree.least_common_ancestor(b, i), a)

