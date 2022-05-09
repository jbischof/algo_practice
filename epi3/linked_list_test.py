import unittest
import linked_list as ll
from linked_list import ListNode

class TestLinkedList(unittest.TestCase):
    def test_add_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.assertListEqual(
                ll.add_numbers(l1, l2).to_list(),
                [7, 0, 8]
        )

        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(9)))
        self.assertListEqual(
                ll.add_numbers(l1, l2).to_list(),
                [7, 0, 3, 1]
        )

        l1 = ListNode(0)
        l2 = ListNode(0)
        self.assertListEqual(ll.add_numbers(l1, l2).to_list(), [0])

