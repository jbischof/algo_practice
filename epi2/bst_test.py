import unittest
import tree as bt
import bst

class BSTTest(unittest.TestCase):
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

  def testIsValid(self):
    # Default tree is valid
    tree = self.ExampleTree()
    self.assertTrue(tree.is_valid())
    # Change value of 'h' to invalidate BST property in way not caught by
    # checking each node's children separately
    tree = self.ExampleTree()
    tree.root.left.right.right.left.data = 10
    self.assertFalse(tree.is_valid())

  def testSearch(self):
    tree = self.ExampleTree()
    self.assertTrue(tree.search(19))
    self.assertTrue(tree.search(31))
    self.assertFalse(tree.search(18))

  def testMinK(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.min_k(4), [2, 3, 5, 7])

  def testMaxK(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.max_k(4), [53, 47, 43, 41])

  def testInorder(self):
    tree = self.ExampleTree()
    self.assertEqual(tree.inorder(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                      37, 41, 43, 47, 53])

  def testInsert(self):
    tree = self.ExampleTree()
    tree.insert(0)
    self.assertEqual(tree.inorder(), [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                      37, 41, 43, 47, 53])
    tree.insert(40)
    self.assertEqual(tree.inorder(), [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                      37, 40, 41, 43, 47, 53])
    # Second insert should have no effect
    tree.insert(40)
    self.assertEqual(tree.inorder(), [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                      37, 40, 41, 43, 47, 53])

  def testDelete(self):
    tree = self.ExampleTree()
    tree.delete(2)
    self.assertEqual(tree.inorder(), [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                      37, 41, 43, 47, 53])
    tree.delete(19)
    self.assertEqual(tree.inorder(), [3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41,
                                      43, 47, 53])
    tree.delete(7)
    self.assertEqual(tree.inorder(), [3, 5, 11, 13, 17, 23, 29, 31, 37, 41, 43,
                                      47, 53])

  def testPageVisitRanker(self):
    visits1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
    visits2 = [5, 5, 5, 5, 5, 6, 6, 1, 3, 2]
    ranker = bst.PageVisitRanker()
    ranker.add_page_visits(visits1)
    self.assertEqual(ranker.top_visited_pages(3), [1, 2, 3])
    ranker.add_page_visits(visits2)
    self.assertEqual(ranker.top_visited_pages(3), [5, 1, 2])

