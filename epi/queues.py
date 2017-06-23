class ArrayQueue():
  def __init__(self, input_list=[], max_size=10):
    self.queue = [0] * max_size
    self.start = None
    self.end = None
    self.max_size = max_size
    self.enqueue_list(input_list)

  def len(self):
    """ Need to account for case where queue empty and where start after end """
    if self.start is None:
      return 0
    elif self.end >= self.start:
      return self.end - self.start + 1
    return (self.max_size - self.start + 1) + self.end + 1

  def enqueue(self, value):
    # Queue is empty, initialize
    if self.start is None:
      self.start, self.end = 0, 0
      self.queue[self.end] = value
      return
    # Need to resize queue if out of space
    if self.end >= self.max_size - 1:
      self.resize()
    self.end += 1
    self.queue[self.end] = value

  def enqueue_list(self, input_list):
    for item in input_list:
      self.enqueue(item)    

  def dequeue(self):
    if self.start is None:
      return None
    elif self.start == self.end:
      # Queue is now empty
      ret = self.queue[self.end]
      self.start, self.end = None, None
      return ret
    self.start += 1
    return self.queue[self.start - 1]

  def resize(self):
    """ Removes dead elements at start of queue and doubles capacity """
    # Do nothing if no dead entries
    if self.start is None:
      return
    # Shift all entries left
    for j in xrange(self.len()):
      self.queue[j] = self.queue[self.start + j]
    self.start, self.end = 0, self.len() - 1
    # Add capacity
    self.queue.extend([0] * self.max_size)
    self.max_size *= 2

  def to_list(self):
    if self.start is None:
      return []
    return [self.queue[i] for i in xrange(self.start, self.end + 1)]

class CircQueue():
  def __init__(self, input_list=[], max_size=10):
    self.queue = [0] * max_size
    self.start, self.end = 0, 0
    self.max_size = max_size
    self.length = 0
    self.enqueue_list(input_list)

  def len(self):
    return self.length

  def enqueue(self, value):
    if not self.length:
      # Initialize empty array
      self.start, self.end = 0, 0
      self.queue[0] = value
      self.length = 1
      return
    if self.length == self.max_size:
      # Queue is full, need to resize
      self.resize()
    # Now know queue has capacity
    self.end = (self.end + 1) % self.max_size
    self.length += 1
    self.queue[self.end] = value

  def enqueue_list(self, input_list):
    for item in input_list:
      self.enqueue(item)    

  def dequeue(self):
    if not self.length:
      return None
    ret = self.queue[self.start]
    self.start = (self.start + 1) % self.max_size
    self.length -= 1
    return ret

  def resize(self):
    """ Removes dead elements and doubles capacity """
    # Do nothing if no entries
    if not self.length:
      return
    self.max_size *= 2
    new_queue = [0] * self.max_size
    # Write active entries into new queue
    for i in xrange(self.length):
      new_queue[i] = self.queue[(self.start + i) % (self.max_size / 2)]
    self.queue = new_queue
    self.start, self.end = 0, self.length - 1

  def to_list(self):
    return [self.queue[(self.start + i) % self.max_size] 
        for i in range(self.length)]

class TwoStackQueue():
  def __init__(self, input_list=[]):
    self.inbox = []
    self.outbox = []
    self.enqueue_list(input_list)

  def enqueue(self, value):
    self.inbox.append(value)

  def enqueue_list(self, input_list):
    for item in input_list:
      self.enqueue(item)    

  def dequeue(self):
    if self.outbox:
      return self.outbox.pop()
    # If outbox empty, make sure entire queue not empty
    if not self.inbox:
      return None
    # If inbox has items, move everything to outbox
    while self.inbox:
      self.outbox.append(self.inbox.pop())
    return self.outbox.pop()

  def len(self):
    return len(self.inbox) + len(self.outbox)
  
  def to_list(self):
    """ Return a list with all elements currently in queue """
    return self.outbox[::-1] + self.inbox
