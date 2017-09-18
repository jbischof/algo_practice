import unittest
import circular_linked_list as cll

class TestCircularLinkedList(unittest.TestCase):
  def ExampleLList(self):
    llist = cll.CircLinkedList(cll.Node('a'))
    llist.add(cll.Node('b'))
    llist.add(cll.Node('c'))
    llist.add(cll.Node('d'))
    llist.add(cll.Node('e'))
    return llist 

  def testSearch(self):
    llist = self.ExampleLList()
    self.assertEqual(llist.search('c').value, 'c')
    self.assertEqual(llist.search('z'), None)

  def testDeleteNode(self):
    llist = self.ExampleLList()
    llist.delete(llist.head)
    self.assertEqual(llist.toList(), ['b', 'c', 'd', 'e'])
    self.assertEqual(llist.head.value, 'b')
    llist = self.ExampleLList()
    llist.delete(llist.search('b'))
    self.assertEqual(llist.toList(), ['a', 'c', 'd', 'e'])
    llist = self.ExampleLList()
    llist.delete(llist.search('e'))
    self.assertEqual(llist.toList(), ['a', 'b', 'c', 'd'])
    self.assertEqual(llist.head.value, 'a')
