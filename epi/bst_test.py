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

  def testSearchWithParent(self):
    tree = self.ExampleTree()
    self.assertEqual(
        tree.search_with_parent(17), 
        (tree.root.left.right.right, tree.root.left.right)) 
    self.assertEqual(
        tree.search_with_parent(13), 
        (tree.root.left.right.right.left, tree.root.left.right.right)) 
    self.assertEqual(
        tree.search_with_parent(53), 
        (tree.root.right.right.right, tree.root.right.right)) 
    self.assertEqual(
        tree.search_with_parent(47), 
        (tree.root.right.right, tree.root.right)) 
    self.assertEqual(tree.search_with_parent(19), (tree.root, None))
    self.assertFalse(tree.search_with_parent(20)) 
    self.assertFalse(tree.search_with_parent(15)) 
    self.assertFalse(tree.search_with_parent(54)) 
    self.assertFalse(tree.search_with_parent(4))

  def testInsert(self):
    tree = self.ExampleTree()
    node4 = bt.Node(4)
    tree.insert(node4)
    self.assertEqual(tree.root.left.left.right.left, node4)
    tree = self.ExampleTree()
    node54 = bt.Node(54)
    tree.insert(node54)
    self.assertEqual(tree.root.right.right.right.right, node54)
    # Check inserting into empty tree
    tree = bst.BST()
    tree.insert(node4)
    self.assertEqual(tree.root, node4)

  def testRemove(self):
    # Remove leaf node
    tree = self.ExampleTree()
    self.assertTrue(tree.root.right.left.right.left.right)
    tree.remove_value(31)
    self.assertTrue(tree.root.right.left.right.left.right is None)
    # Remove node with one child
    tree = self.ExampleTree()
    self.assertEqual(tree.root.right.left.right.left.value, 29)
    tree.remove_value(29)
    self.assertEqual(tree.root.right.left.right.left.value, 31)
    # Remove node with two children
    tree = self.ExampleTree()
    self.assertEqual(tree.root.right.value, 43)
    tree.remove_value(43)
    self.assertEqual(tree.root.right.value, 47)
    self.assertEqual(tree.root.right.right.value, 53)
    self.assertEqual(tree.root.right.left.value, 23)

  def testNextLargest(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.next_largest(0), tree.root.left.left.left)
    self.assertEqual(tree.next_largest(54), None)
    self.assertEqual(tree.next_largest(17), tree.root)
    self.assertEqual(tree.next_largest(31), tree.root.right.left.right)
    self.assertEqual(tree.next_largest(24), tree.root.right.left.right.left)

  def testKLargest(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.k_largest(1), [53])
    self.assertEqual(tree.k_largest(4), [53, 47, 43, 41])

  def testKSmallest(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.k_smallest(1), [2])
    self.assertEqual(tree.k_smallest(4), [2, 3, 5, 7])

  def testWebpageIndex(self):
    index = bst.WebpageIndex()
    index.update_list(
       [bst.Webpage(i) for i in [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5]])
    self.assertEqual(index.top_k_visited(3), [1, 2, 4]) 
    # Make '5' most visited page (by one visit)
    index.update_list([bst.Webpage(i) for i in [5] * 5])
    self.assertEqual(index.top_k_visited(3), [5, 1, 2]) 
