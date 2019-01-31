import unittest
import linked_list as ll


class DoublyLinkedListTest(unittest.TestCase):
  def testInit(self):
    a = ll.Node('a')
    d = ll.DoublyLinkedList(a)
    self.assertEqual(d.values(), ['a'])
    self.assertEqual(d.head, a)
    self.assertEqual(d.tail, a)

  def testAppend(self):
    dl = ll.DoublyLinkedList()
    a, b, c, d = ll.Node('a'), ll.Node('b'), ll.Node('c'), ll.Node('d')
    dl.append_list([a, b, c, d])
    self.assertEqual(dl.values(), ['a', 'b', 'c', 'd'])
    self.assertEqual(dl.head, a)
    self.assertEqual(dl.tail, d)

  def testInsertAtHead(self):
    dl = ll.DoublyLinkedList()
    a, b, c, d = ll.Node('a'), ll.Node('b'), ll.Node('c'), ll.Node('d')
    e = ll.Node('e')
    dl.insert_at_head(a)
    self.assertEqual(dl.head, a)
    self.assertEqual(dl.tail, a)
    dl.append_list([b, c, d])
    self.assertEqual(dl.values(), ['a', 'b', 'c', 'd'])
    dl.insert_at_head(e)
    self.assertEqual(dl.values(), ['e', 'a', 'b', 'c', 'd'])

  def testDelete(self):
    dl = ll.DoublyLinkedList()
    a, b, c, d = ll.Node('a'), ll.Node('b'), ll.Node('c'), ll.Node('d')
    dl.append_list([a, b, c, d])
    self.assertEqual(dl.values(), ['a', 'b', 'c', 'd'])
    dl.delete(b)
    self.assertEqual(dl.values(), ['a', 'c', 'd'])
    dl.delete(a)
    self.assertEqual(dl.values(), ['c', 'd'])
    self.assertEqual(dl.head, c)
    dl.delete(d)
    self.assertEqual(dl.values(), ['c'])
    self.assertEqual(dl.head, c)
    self.assertEqual(dl.tail, c)

