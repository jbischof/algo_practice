"""Experiment with circular linked list, where  tail is linked to the head."""

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None


class CircLinkedList(object):
  def __init__(self, head=None):
    self.head = head
    if self.head:
      self.head.next = self.head

  def toList(self):
    if not self.head:
      return []
    ret = [self.head.value]
    next_node = self.head
    while next_node.next != self.head:
      next_node = next_node.next
      ret.append(next_node.value)
    return ret

  def add(self, node):
    # If no head, node is head and links to itself
    if not self.head:
      self.head = node
      self.head.next = node
      return
    # Otherwise last node is one linked to head
    next_node = self.head
    while next_node.next != self.head:
      next_node = next_node.next
    next_node.next = node
    node.next = self.head


  def search(self, value):
    """Search for specific value.
    
    Args:
      value: value to search for
    Returns:
      Node with value if found or None.
    """

    if not self.head:
      return None
    next_node = self.head
    while next_node.value != value:
      next_node = next_node.next
      if next_node == self.head:
        return None
    return next_node


  def delete(self, node):
    """Deletes node from list."""
    isHead, isTail = node == self.head, node.next == self.head
    if isHead and isTail:
      self.head = None
      return
    # Copy next node info to this node and remove next node
    node.value = node.next.value
    node.next = node.next.next
    # If deleted node the tail, new value is for the head
    if isTail:
      self.head = node
