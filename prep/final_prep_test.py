import unittest
import final_prep as fp
import numpy as np
import sys
sys.path.append('../epi/')
import binary_tree as bt

class TestFinalPrep(unittest.TestCase):
  def testLongestTwoCharSubstring(self):
    self.assertEqual(fp.longest_twochar_substr('ababcbcbaaabbdef'),
                     'baaabb')
    self.assertEqual(fp.longest_Mchar_substr('ababcbcbaaabbdef', 2),
                     'baaabb')

  def testIsDeckValid(self):
    deck = [1, 1, 2, 2, 3, 3, 3, 4, 5]
    self.assertTrue(fp.is_deck_valid(deck))
    # Remove one of needed 3s
    deck.pop(4)
    self.assertFalse(fp.is_deck_valid(deck))

  def testIsRoot(self):
    # A genuine tree
    adj_list = {
        'a': set('bc'),
        'b': set('de'),
        'c': set('f'),
        'd': set(),
        'e': set(),
        'f': set()
    }
    self.assertTrue(fp.is_tree(adj_list))
    # Add cycle
    adj_list['c'].add('e')
    self.assertFalse(fp.is_tree(adj_list))
    adj_list['c'].remove('e')
    # Add other tree
    adj_list['g'] = set('hi')
    adj_list['h'] = set()
    adj_list['i'] = set()
    self.assertFalse(fp.is_tree(adj_list))

  def testIsSubsetSum(self):
    self.assertTrue(fp.is_subset_sum([8, 6, 7, 5, 3, 10, 9], 15))
    self.assertFalse(fp.is_subset_sum([11, 6, 5, 1, 7, 13, 12], 15))
    self.assertTrue(fp.is_subset_sum([11, 6, 5, 1, 7, 13, 15], 15))

  def testPartitionArrayWeight(self):
    a = [5, 6, 11, 20, 3, 11, 6, 10, 2, 2, 1]
    self.assertEqual(fp._partition_array_weight(a, 4, 22), [
        fp.Partition(2, 22),
        fp.Partition(3, 20),
        fp.Partition(6, 20),
        fp.Partition(10, 15)])
    self.assertFalse(fp._partition_array_weight(a, 4, 21))
    self.assertEqual(fp.min_cargo_capacity(a, 4), 22)

  def testMultinomialRNG(self):
    probs = [0.1, 0.5, 0.4]
    self.assertEqual(fp.multinomial_rng(probs, 0.05), 0)
    self.assertEqual(fp.multinomial_rng(probs, 0.5), 1)
    self.assertEqual(fp.multinomial_rng(probs, 0.7), 2)
    self.assertEqual(fp.multinomial_rng(probs, 0.99), 2)

  def testLastUniqueInt(self):
    lui = fp.LastUniqueInt()
    self.assertEqual(lui.update_last_unique(0), 0)
    self.assertEqual(lui.update_last_unique(1), 1)
    self.assertEqual(lui.update_last_unique(2), 2)
    self.assertEqual(lui.update_last_unique(1), 2)
    self.assertEqual(lui.update_last_unique(2), 0)
    self.assertEqual(lui.update_last_unique(3), 3)

  def testRemoveCharCasePairs(self):
    b = bytearray('abBbcCk')    
    len_new_b = fp.remove_char_case_pairs(b)
    self.assertEqual(b[:len_new_b], 'abk')
    b = bytearray('abBbcCxKk')    
    len_new_b = fp.remove_char_case_pairs(b)
    self.assertEqual(b[:len_new_b], 'abx')
    b = bytearray('BbcCKka')    
    len_new_b = fp.remove_char_case_pairs(b)
    self.assertEqual(b[:len_new_b], 'a')
    b = bytearray('BbcCKk')    
    len_new_b = fp.remove_char_case_pairs(b)
    self.assertEqual(len_new_b, None)
    # Repeated removal necessary
    b = bytearray('abCcBk')    
    len_new_b = fp.remove_char_case_pairs(b)
    self.assertEqual(b[:len_new_b], 'ak')
    
  def testFurthestLeafDist(self):
    a = fp.NaryNode('a')
    b = fp.NaryNode('b')
    c = fp.NaryNode('c')
    d = fp.NaryNode('d')
    e = fp.NaryNode('e')
    f = fp.NaryNode('f')
    g = fp.NaryNode('g')
    h = fp.NaryNode('h')
    i = fp.NaryNode('i')
    j = fp.NaryNode('j')
    k = fp.NaryNode('k')
    a.edges.extend([fp.NaryEdge(b, 6), 
                    fp.NaryEdge(c, 5),
                    fp.NaryEdge(d, 2)])
    b.edges.append(fp.NaryEdge(e, 1)) 
    c.edges.extend([fp.NaryEdge(f, 2), 
                    fp.NaryEdge(g, 7),
                    fp.NaryEdge(h, 3)])
    d.edges.extend([fp.NaryEdge(i, 11), 
                    fp.NaryEdge(j, 3)])
    j.edges.append(fp.NaryEdge(k, 5)) 
    self.assertEqual(fp.furthest_leaf_dist(a), 13)


  def FADTree(self):
    a = bt.Node('a')
    b = bt.Node('b')
    c = bt.Node('c')
    d = bt.Node('d')
    e = bt.Node('e')
    f = bt.Node('f')
    g = bt.Node('g')
    h = bt.Node('h')
    i = bt.Node('i')
    j = bt.Node('j')
    f.left = b
    f.right = g
    b.left = a
    b.right = d
    d.left = c
    d.right = e
    g.right = i
    i.left = h
    h.right = j 
    return f

  def testForestAfterDeletion(self):
    root = self.FADTree()
    forest = fp.forest_after_delete(root, set('bi'))
    self.assertItemsEqual(
            [node.value for node in forest],
            ['f', 'a', 'd', 'h'])
    # Check pointer cleanup
    self.assertEqual(root.left, None)
    self.assertEqual(root.right.right, None)

    # Delete non-consecutive nodes in same subtree
    root = self.FADTree()
    forest = fp.forest_after_delete(root, set('bid'))
    self.assertItemsEqual(
            [node.value for node in forest],
            ['f', 'a', 'c', 'e', 'h'])

    # Delete two consecutive nodes
    root = self.FADTree()
    forest = fp.forest_after_delete(root, set('bih'))
    self.assertItemsEqual(
            [node.value for node in forest],
            ['f', 'a', 'd', 'j'])

    # Delete the root
    root = self.FADTree()
    forest = fp.forest_after_delete(root, set('f'))
    self.assertItemsEqual(
            [node.value for node in forest],
            ['b', 'g'])

  def testDistinctOverlappingIntervals(self):
   self.assertEqual(
       fp.distinct_overlapping_intervals([
           fp.Interval(0, 4, set('x')),
           fp.Interval(5, 8, set('y')),
           fp.Interval(3, 6, set('z'))]),
        [
           fp.Interval(0, 3, set('x')),
           fp.Interval(3, 4, set('xz')),
           fp.Interval(4, 5, set('z')),
           fp.Interval(5, 6, set('zy')),
           fp.Interval(6, 8, set('y'))]
        )


