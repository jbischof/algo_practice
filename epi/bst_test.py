import unittest
import bst
import binary_tree as bt

class TestBST(unittest.TestCase):
  def ExampleTree(self):
    a = bt.Node(19)
    b = bt.Node(7)
    c = bt.Node(3)
    d = bt.Node(2)
    e = bt.Node(5)
    f = bt.Node(11)
    g = bt.Node(17)
    h = bt.Node(13)
    i = bt.Node(43)
    j = bt.Node(23)
    k = bt.Node(37)
    l = bt.Node(29)
    m = bt.Node(31)
    n = bt.Node(41)
    o = bt.Node(47)
    p = bt.Node(53)
    tree = bst.BST(a)
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
    
  def testCheckValid(self):
    # Default tree is valid
    tree = self.ExampleTree()
    self.assertTrue(tree.check_valid())
    # Change value of 'h' to invalidate BST property in way not caught by
    # checking each node's children separately
    tree.root.left.right.right.left.value = 10
    self.assertFalse(tree.check_valid())

  def testSearch(self):
    tree = self.ExampleTree()
    self.assertTrue(tree.search(17)) 
    self.assertTrue(tree.search(13)) 
    self.assertTrue(tree.search(53)) 
    self.assertTrue(tree.search(47)) 
    self.assertTrue(tree.search(19)) 
    self.assertFalse(tree.search(20)) 
    self.assertFalse(tree.search(15)) 
    self.assertFalse(tree.search(54)) 
    self.assertFalse(tree.search(4))

  def testNextLargest(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.next_largest(0), 2)
    self.assertEqual(tree.next_largest(54), None)
    self.assertEqual(tree.next_largest(17), 19)
    self.assertEqual(tree.next_largest(31), 37)
    self.assertEqual(tree.next_largest(24), 29)
