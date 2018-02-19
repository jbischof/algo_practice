"""Stack and queue problems."""

class StackWithMin(object):
  """Stack where min can be computed in O(1) time."""

  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return not self.stack

  def peek(self):
    if self.isEmpty():
      return None
    else:
      return self.stack[-1][0]

  def min(self):
    if self.isEmpty():
      return None
    else:
      return self.stack[-1][1]

  def push(self, value):
    if self.isEmpty():
      self.stack.append((value, value))
      return
    if value < self.min():
      self.stack.append((value, value))
    else:
      self.stack.append((value, self.min()))

  def pop(self):
    if self.isEmpty():
      return None
    return self.stack.pop()[0]
    

class QueueFromStack(object):
  """Queue class built from stacks."""

  def __init__(self):
    self.inbox = []
    self.outbox = []

  def push(self, value):
    self.inbox.append(value)

  def pop(self):
    if self.outbox:
      return self.outbox.pop()
    if self.inbox:
      while self.inbox:
        self.outbox.append(self.inbox.pop())
      return self.outbox.pop() 
    return None

  def peek(self):
    if self.outbox:
      return self.outbox[-1]
    if self.inbox:
      return self.inbox[0]
    return None


class Stack(object):
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return not self.stack

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if self.isEmpty():
      return None
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return None
    return self.stack[-1]

  def sort(self):
    """Sort a stack using an extra stack.
    
    Time complexity: O(N^2)
    Space complexity: O(N)

    Args:
      a: An array representing a stack
    Returns:
      Array representing sorted stack.
    """

    sort_stack = Stack() 

    while not self.isEmpty():
      num_pop = 0
      curr = self.pop()
      while not sort_stack.isEmpty() and sort_stack.peek() < curr:
        num_pop += 1
        self.push(sort_stack.pop())
      sort_stack.push(curr)
      while num_pop:
        sort_stack.push(self.pop())
        num_pop -= 1

    self.stack = sort_stack.stack


    




