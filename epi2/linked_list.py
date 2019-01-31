"""Linked list problems."""

class Node(object):
  def __init__(self, data=None):
    self.prev = None
    self.next = None
    self.data = data 

class DoublyLinkedList(object):
  def __init__(self, head=None):
    self.head = head
    self.tail = head

  def insert_at_head(self, node):
    # Clear any previous connection data
    node.prev, node.next = None, None
    if self.head:
      self.head.prev = node
      node.next = self.head
      self.head = node
    else:
      self.head = node
      self.tail = node
    return

  def append(self, node):
    # Clear any previous connection data
    node.prev, node.next = None, None
    if not self.head:
      self.head, self.tail = node, node
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = node
    node.prev = curr
    self.tail = node

  def append_list(self, a):
    """Append iterable of Node objects."""

    for node in a:
      self.append(node)

  def delete(self, node):
    if node == self.head:
      self.head = self.head.next
      if self.head:
        self.head.prev = None
        if not self.head.next:
          self.tail = self.head
      return
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    else:
      self.tail = node.prev
    return

  def values(self):
    """Return values in list."""

    values = []
    curr = self.head
    while curr:
      values.append(curr.data)
      curr = curr.next
    return values
