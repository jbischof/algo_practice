"""Linked list problems."""

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    
  def search(self, value):
    """Return first node with value `value`.
    
    Returns `None` if value not found.
    """

    curr = self.head
    while curr:
      if curr.value == value:
        return curr
      curr = curr.next
    return None

  def add(self, node):
    """Add a node."""

    if not self.head:
      self.head = node
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = node

  def add_value(self, value):
    """Add a node with value `value`."""

    new_node = Node(value)
    self.add(new_node)

  def add_from_list(self, values):
    """Add nodes from values in list `values`."""

    for value in values:
      self.add_value(value)

  def add_to_head(self, node):
    """Add node to head of list."""

    old_head = self.head
    self.head = node
    self.head.next = old_head

  def add_value_to_head(self, value):
    """Add node with value `value` to head of list."""

    new_head = Node(value)
    self.add_to_head(new_head)

  def to_list(self):
    """Return contents as Python list."""

    curr = self.head
    ret = []
    while curr:
      ret.append(curr.value)
      curr = curr.next
    return ret

  def len(self):
    """Length of current list."""
     
    curr = self.head
    count = 0
    while curr:
      count += 1
      curr = curr.next
    return count

  def delete(self, value):
    """Delete first node with value `value` if exists."""

    if not self.head:
      return
    if self.head.value == value:
      self.head = self.head.next
      return
    prev, curr = self.head, self.head.next
    while curr:
      if curr.value == value:
        prev.next = curr.next
        return
      prev, curr = curr, curr.next

  def remove_dups(self):
    """Remove any duplicate values from list.
    
    Time complexity: O(N)
    Space complexity: O(N)
    """

    if not self.head:
      return
    seen = set([self.head.value])
    prev, curr = self.head, self.head.next
    while curr:
      if curr.value in seen:
        prev.next = curr.next
        curr = prev.next
      else:
        seen.add(curr.value)
        prev, curr = curr, curr.next

  def remove_dups_no_space(self):
    """Remove any duplicate values from list without using extra space.
    
    Time complexity: O(N^2)
    Space complexity: O(1)
    """

    curr = self.head
    while curr:
      # Send runner down rest of list looking for dups
      prev_run, run = curr, curr.next
      while run:
        if run.value == curr.value:
          prev_run.next = run.next
          run = prev_run.next
        else:
          prev_run, run = run, run.next
      curr = curr.next

  def kth_to_last(self, k):
    """Return kth to last Node from end of list.

    Returns `None` if list less than length k.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    if not self.head:
      return None
    # Send first runner k positions ahead. Can return answer if reach end.
    first, second = self.head, self.head
    for i in xrange(k):
      first = first.next
      if not first:
        return None
    # Move runners together until hit end
    while first.next:
      first, second = first.next, second.next
    return second

  def delete_nontail_node(self, node):
    """Delete non-tail node in O(1) time."""
    
    if node == self.head:
      self.head = node.next
      return
    if node.next is None:
      return
    node.value = node.next.value
    node.next = node.next.next

  def partition(self, pivot):
    """Place values in array less than pivot before others.

    Time complexity: O(N)
    Space complexity: O(N) but could be made O(1)
    """

    lt_list = LinkedList() 
    gte_list = LinkedList()
    # Maintain pointer to tail of lt list
    lt_tail = None

    curr = self.head
    while curr:
      next = curr.next
      curr.next = None
      if curr.value < pivot:
        lt_list.add(curr)
        lt_tail = curr
      else:
        gte_list.add(curr)
      curr = next
    
    # Reconstruct single list
    self.head = lt_list.head or gte_list.head
    if lt_list.head:
      lt_tail.next = gte_list.head

  def reverse(self):
    """Reverse list.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    rev_list = LinkedList()
    curr = self.head
    while curr:
      next = curr.next
      curr.next = None
      rev_list.add_to_head(curr)
      curr = next
    self.head = rev_list.head

  def isPalindrome(self):
    """Detect if current list is a palindrome.
    
    Time complexity: O(N)
    Space complexity: O(1)
    """

    # Last node of first list of half_len from end
    half_len = self.len() // 2
    last_of_first = self.kth_to_last(half_len)
    # Make second list starting from next node
    second_head = last_of_first.next
    last_of_first.next = None
    second = LinkedList(second_head)
    # Reverse second list and compare to first
    second.reverse()
    first_node = self.head
    second_node = second.head
    ret = True
    for i in xrange(half_len):
      if not first_node.value == second_node.value:
        ret = False
        break
      first_node, second_node = first_node.next, second_node.next
    # Reassemble original list
    second.reverse()
    last_of_first.next = second.head
    return ret


def addLinkedListInts(l1, l2):
  """Add integers using LinkedList representation.

  The i-th position in each list with value k equals pow(10, i) * k.

  Args:
    l1, l2: LinkedList objects
  Returns:
    LinkedList with sum in same integer representation.
  """

  sum_list = LinkedList()
  l1_curr, l2_curr = l1.head, l2.head
  carry_sum = 0

  while l1_curr or l2_curr or carry_sum:
    curr_sum = carry_sum
    if l1_curr:
      curr_sum += l1_curr.value
      l1_curr = l1_curr.next
    if l2_curr:
      curr_sum += l2_curr.value
      l2_curr = l2_curr.next
    pos_sum = curr_sum % 10
    carry_sum = curr_sum // 10
    sum_list.add_value(pos_sum)
  return sum_list
  
    
