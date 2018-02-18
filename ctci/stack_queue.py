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

