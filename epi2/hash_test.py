import unittest
import hash

class HashTest(unittest.TestCase):
  def testIsPermPalindrome(self):
    self.assertTrue(hash.is_perm_palindrome('fgfghh'))
    self.assertTrue(hash.is_perm_palindrome('fgfghhi'))
    self.assertFalse(hash.is_perm_palindrome('fgfghhij'))


  def testLRUCache(self):
    lru = hash.LRUCache(5)
    lru.insert('a', 1)
    lru.insert('b', 2)
    lru.insert('c', 3)
    lru.insert('d', 4)
    lru.insert('e', 5)
    self.assertEqual(lru.keys(), ['e', 'd', 'c', 'b', 'a'])
    # Update existing key: check moved to the front
    lru.insert('a', 1)
    self.assertEqual(lru.keys(), ['a', 'e', 'd', 'c', 'b'])
    # Add key when over capacity: check that LRU deleted
    lru.insert('f', 6)
    self.assertEqual(lru.keys(), ['f', 'a', 'e', 'd', 'c'])
    # Check lookup
    self.assertTrue(lru.lookup('f')[0])
    self.assertEqual(lru.lookup('f')[1], 6)
    self.assertFalse(lru.lookup('g')[0])
    # Check deletion of random key
    lru.erase('f')
    self.assertEqual(lru.keys(), ['a', 'e', 'd', 'c'])

  def testFindClosestRepeat(self):
    self.assertEqual(hash.find_closest_repeat(
        ['a', 'b', 'a', 'c', 'd', 'e', 'c']), 'a') 

  def testFindKeywordSpan(self):
    sentence = 'd a b c d a b b a c d b a'.split(' ')
    self.assertEqual(hash.find_keyword_span(sentence, set(['b', 'd'])),
                     (10, 11))
