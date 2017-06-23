import linked_list as ll
import unittest

class TestLinkedList(unittest.TestCase):
	def exampleList(self):
		llist = ll.LinkedList.from_list([0, 2, 5, 7])
		return llist

	def testFromToList(self):
		llist = ll.LinkedList.from_list([0, 2, 5, 7])
		self.assertEqual(llist.to_list(), [0, 2, 5, 7])

	def testInsertAtTail(self):
		# Empty list
		llist = ll.LinkedList()
		llist.insert_at_tail(ll.Node(10))
		self.assertEqual(llist.to_list(), [10])
		self.assertEqual(llist.head.value, 10)
		self.assertEqual(llist.tail.value, 10)
		# Normal list
		llist = self.exampleList()
		llist.insert_at_tail(ll.Node(10))
		self.assertEqual(llist.to_list(), [0, 2, 5, 7, 10])
		self.assertEqual(llist.tail.value, 10)

	def testSearch(self):
		# Normal list entry
		llist = self.exampleList()
		found_node = llist.search(5)
		self.assertEqual(found_node.value, 5)
		# Tail of list
		found_node = llist.search(7)
		self.assertEqual(found_node.value, 7)
		# Non-existent entry
		found_node = llist.search(10)
		self.assertEqual(found_node, None)

	def testInsertAfter(self):
		llist = self.exampleList()
		found_node = llist.search(5)
		llist.insert_after(found_node, ll.Node(10))
		self.assertEqual(llist.to_list(), [0, 2, 5, 10, 7])
		self.assertEqual(llist.tail.value, 7)
		# Test insertion after tail
		found_node = llist.search(7)
		llist.insert_after(found_node, ll.Node(12))
		self.assertEqual(llist.to_list(), [0, 2, 5, 10, 7, 12])
		self.assertEqual(llist.tail.value, 12)

	def testInsertAtHead(self):
		llist = self.exampleList()
		llist.insert_at_head(ll.Node(10))
		self.assertEqual(llist.to_list(), [10, 0, 2, 5, 7])
		self.assertEqual(llist.head.value, 10)
		self.assertEqual(llist.tail.value, 7)
		# Test insertion in empty list
		llist = ll.LinkedList()
		llist.insert_at_head(ll.Node(10))
		self.assertEqual(llist.to_list(), [10])
		self.assertEqual(llist.head.value, 10)
		self.assertEqual(llist.tail.value, 10)

	def testDeleteAfter(self):
		llist = self.exampleList()
		found_node = llist.search(2)
		llist.delete_after(found_node)
		self.assertEqual(llist.to_list(), [0, 2, 7])
		self.assertEqual(llist.tail.value, 7)
		# Test deletion of tail
		llist = self.exampleList()
		found_node = llist.search(5)
		llist.delete_after(found_node)
		self.assertEqual(llist.to_list(), [0, 2, 5])
		self.assertEqual(llist.tail.value, 5)
		# Test deletion after tail (nothing should happen)
		llist = self.exampleList()
		found_node = llist.search(7)
		llist.delete_after(found_node)
		self.assertEqual(llist.to_list(), [0, 2, 5, 7])
		self.assertEqual(llist.tail.value, 7)

	def testPop(self):
		n1, n2, n3 = ll.Node(1), ll.Node(2), ll.Node(3)
		llist = ll.LinkedList(n1)
		llist.insert_at_tail(n2)
		llist.insert_at_tail(n3)
		res = llist.pop()
		self.assertEqual(res.value, n1.value)
		self.assertEqual(res.next, None)
		self.assertEqual(n2.next, n3)

	def testListTraverse(self):
		llist = ll.LinkedList.from_list([2, 3, 4, 5, 7, 10, 15])
		node0 = llist.traverse(0)
		node1 = llist.traverse(2, node0)
		node2 = llist.traverse(3, node1)
		node3 = llist.traverse(3, node2)
		self.assertEqual(node0.value, 2)
		self.assertEqual(node1.value, 4)
		self.assertEqual(node2.value, 10)
		self.assertTrue(node3 is None)

	def testReverseSubset(self):
		llist = ll.LinkedList.from_list([2, 3, 4, 5, 7, 10, 15])
		llist.reverse_subset(1, 4)
		self.assertEqual(llist.to_list(), [2, 7, 5, 4, 3, 10, 15])
		# Subset starting from head
		llist = ll.LinkedList.from_list([2, 3, 4, 5, 7, 10, 15])
		llist.reverse_subset(0, 4)
		self.assertEqual(llist.to_list(), [7, 5, 4, 3, 2, 10, 15])
		# Subset of length one
		llist = ll.LinkedList.from_list([2, 3, 4, 5, 7, 10, 15])
		llist.reverse_subset(4, 4)
		self.assertEqual(llist.to_list(), [2, 3, 4, 5, 7, 10, 15])

	def testMergeSortedLists(self):
		# Clean case
		llist1 = ll.LinkedList.from_list([3, 5, 7])
		llist2 = ll.LinkedList.from_list([2, 4, 10, 15])
		merge_list = ll.merge_sorted_linked_list(llist1, llist2)
		self.assertEqual(merge_list.to_list(), [2, 3, 4, 5, 7, 10, 15])
		# One list smaller completely than other
		llist1 = ll.LinkedList.from_list([-7, -5, -3, 0])
		llist2 = ll.LinkedList.from_list([2, 4, 10, 15])
		merge_list = ll.merge_sorted_linked_list(llist1, llist2)
		self.assertEqual(merge_list.to_list(), [-7, -5, -3, 0, 2, 4, 10, 15])
		# Some equal values
		llist1 = ll.LinkedList.from_list([2, 3, 5, 7, 10])
		llist2 = ll.LinkedList.from_list([2, 4, 10, 15])
		merge_list = ll.merge_sorted_linked_list(llist1, llist2)
		self.assertEqual(merge_list.to_list(), [2, 2, 3, 4, 5, 7, 10, 10, 15])
		# One list empty
		llist1 = ll.LinkedList.from_list([])
		llist2 = ll.LinkedList.from_list([2, 4, 10, 15])
		merge_list = ll.merge_sorted_linked_list(llist1, llist2)
		self.assertEqual(merge_list.to_list(), [2, 4, 10, 15])
		# Both lists empty
		llist1 = ll.LinkedList.from_list([])
		llist2 = ll.LinkedList.from_list([])
		merge_list = ll.merge_sorted_linked_list(llist1, llist2)
		self.assertEqual(merge_list.to_list(), [])

	def testCheckCycles(self):
		llist = ll.LinkedList.from_list([2, 3, 4, 5, 7, 10, 15])
		# First check that no cycles found in regular list
		has_cycle, loc = llist.check_cycles()
		self.assertFalse(has_cycle)
		self.assertTrue(loc is None)
		self.assertTrue(llist.find_cycle() is None)
		# Add a cycle from the tail
		cyc_start = llist.search(5)
		llist.tail.next = cyc_start
		has_cycle, loc = llist.check_cycles()
		self.assertTrue(has_cycle)
		self.assertTrue(loc is not None)
		# Find location of cycle
		self.assertEqual(llist.find_cycle(), cyc_start)
