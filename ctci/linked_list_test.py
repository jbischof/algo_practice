import linked_list as llist
import unittest

class LinkedListTest(unittest.TestCase):
  def testInit(self):
    x = llist.LinkedList(llist.Node(10))
    self.assertEqual(x.head.value, 10)
    self.assertEqual(x.head.next, None)

  def testAdd(self):
    x = llist.LinkedList()
    x.add_value(10)
    x.add_value(3)
    self.assertEqual(x.head.value, 10)
    self.assertEqual(x.head.next.value, 3)

  def testAddList(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3])
    self.assertEqual(x.head.value, 10)
    self.assertEqual(x.head.next.value, 3)
  
  def testAddtoHead(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3])
    new_head = llist.Node(13)
    x.add_to_head(new_head)
    self.assertEqual(x.to_list(), [13, 10, 3])

  def testToList(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3])
    self.assertEqual(x.to_list(), [10, 3])

  def testLen(self):
    x = llist.LinkedList()
    self.assertEqual(x.len(), 0)
    x.add_from_list([10, 3])
    self.assertEqual(x.len(), 2)

  def testDelete(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 4, 23])
    x.delete(32)
    self.assertEqual(x.to_list(), [10, 3, 4, 23])
    x.delete(3)
    self.assertEqual(x.to_list(), [10, 4, 23])
    x.delete(23)
    self.assertEqual(x.to_list(), [10, 4])
    x.delete(10)
    self.assertEqual(x.to_list(), [4])
    x.delete(4)
    self.assertEqual(x.to_list(), [])

  def testRemoveDups(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 10, 4, 23, 42, 4])
    x.remove_dups()
    self.assertEqual(x.to_list(), [10, 3, 4, 23, 42])

  def testRemoveDupsNoSpace(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 10, 4, 23, 42, 4])
    x.remove_dups_no_space()
    self.assertEqual(x.to_list(), [10, 3, 4, 23, 42])

  def testKthToLast(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 1, 4, 23, 42, 9])
    self.assertEqual(x.kth_to_last(0).value, 9)
    self.assertEqual(x.kth_to_last(1).value, 42)
    self.assertEqual(x.kth_to_last(3).value, 4)

  def testDeleteNonTailNode(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 1, 4, 23, 42, 9])
    # Need to write method to find node with value
    pass

  def testPartition(self):
    x = llist.LinkedList()
    x.add_from_list([10, 3, 1, 4, 23, 42, 9])
    x.partition(5)
    self.assertEqual(x.to_list(), [3, 1, 4, 10, 23, 42, 9])
    # All values greater than partition
    x = llist.LinkedList()
    x.add_from_list([10, 3, 1, 4, 23, 42, 9])
    x.partition(0)
    self.assertEqual(x.to_list(), [10, 3, 1, 4, 23, 42, 9])
    # All values less than partition
    x = llist.LinkedList()
    x.add_from_list([10, 3, 1, 4, 23, 42, 9])
    x.partition(50)
    self.assertEqual(x.to_list(), [10, 3, 1, 4, 23, 42, 9])

  def testRemoveDupsNoSpace(self):
    x = llist.LinkedList()
    x.add_from_list([3, 10, 23, 42, 4])
    x.reverse()
    self.assertEqual(x.to_list(), [4, 42, 23, 10, 3])

  def testIsPalindrome(self):
    # Odd length palindrome
    x = llist.LinkedList()
    pal1 = ['m', 'a', 'd', 'a', 'm', 'i', 'm', 'a', 'd', 'a', 'm']
    x.add_from_list(pal1)
    self.assertTrue(x.isPalindrome())
    self.assertEqual(x.to_list(), pal1)
    # Even length palindrome
    x = llist.LinkedList()
    pal2 = ['a', 'n', 'n', 'a']
    x.add_from_list(pal2)
    self.assertTrue(x.isPalindrome())
    self.assertEqual(x.to_list(), pal2)
    # Not a palindrome
    x = llist.LinkedList()
    pal3 = ['a', 'n', 'n', 'i', 'e']
    x.add_from_list(pal3)
    self.assertFalse(x.isPalindrome())
    self.assertEqual(x.to_list(), pal3)

  def testAddLinkedListInts(self):
    l1, l2 = llist.LinkedList(), llist.LinkedList()
    l1.add_from_list([3, 4, 5])
    l2.add_from_list([8, 4, 7, 9])
    self.assertEqual(llist.addLinkedListInts(l1, l2).to_list(),
                     [1, 9, 2, 0, 1])
    l1, l2 = llist.LinkedList(), llist.LinkedList()
    l1.add_from_list([3])
    l2.add_from_list([8, 9, 9, 9])
    self.assertEqual(llist.addLinkedListInts(l1, l2).to_list(),
                     [1, 0, 0, 0, 1])
