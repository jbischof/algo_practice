"""Linked List problems."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        ret = [self.val]
        child = self.next
        while child:
            ret.append(child.val)
            child = child.next
        return ret

def add_numbers(l1, l2):
    """
    Add two linked list numbers in reverse order

    Example: 
    [2, 4, 3]
    [5, 6, 4]
    digits, carry, nd, ans
    -,      0,     -,  None
    2, 5,   0,     7,  [7]
    4, 6,   1,     0,  [7, 0]
    3, 4,   0,     8,  [7, 0, 8]
    """
    
    ans = None
    carry = 0
    while l1 or l2 or carry:
        next_digit = carry
        if l1:
            next_digit += l1.val
            l1 = l1.next
        if l2:
            next_digit += l2.val
            l2 = l2.next
        next_item = ListNode(next_digit % 10)
        carry = next_digit // 10
        if ans:
            ans.next = next_item
            ans = ans.next
        else:
            ans = next_item
            first = ans
    return first
