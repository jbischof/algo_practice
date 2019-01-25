"""Stack of problems."""
import collections

def rpn(s):
  """Evaluate RPN expression.

  Time complexity: O(n)
  Space complexity: O(n)
  
  Args:
    s: String with RPN expression

  Returns: Float with result.
  """

  DELIM = ','
  OPERATORS = '+-*/'
  stack = []

  for val in s.split(DELIM):
    if val in OPERATORS:
      if len(stack) < 2:
        raise ValueError('Expression not proper RPN.')
      num1, num2 = stack.pop(), stack.pop()
      if val == '+':
        stack.append(num2 + num1)
      elif val == '-':
        stack.append(num2 - num1) 
      elif val == '*':
        stack.append(num2 * num1) 
      else:
        stack.append(num2 / num1) 
    else:
      stack.append(int(val))
  return stack[0]


def valid_parens(s):
  """Check is parens in string valid."""

  PARENS = {')': '(', ']': '[', '}': '{'}
  stack = []

  for char in s:
    if char in PARENS:
      # Close parens unmatched
      if stack.pop() != PARENS[char]:
        return False
    elif char in PARENS.values():
      stack.append(char)
  # Open parens left unmatched
  if stack:
    return False
  return True


def normalize_path(s):
  """Return the shortest equivalent version of path string.

  Args:
    s: Relative or absolute unix path

  Returns:
    Normalized path

  Raises:
    ValueError: path not valid.
  """

  abs_path = (s[0] == '/')
  stack = []
  a = s.split('/')

  for f in a:
    if f.isalnum():
      stack.append(f)
    elif f == '..':
      # Deal with parent dir '..'
      if stack and stack[-1] == '..':
        stack.append('..')
      elif stack and stack[-1] != '..':
        stack.pop()
      elif not stack and not abs_path:
        stack.append('..')
      else:
        raise ValueError('Invalid path')
    elif f == '.' or f == '':
      # Other valid chars
      continue
    else:
      raise ValueError('Invalid character ' + f + ' in path.')

  return '/' + '/'.join(stack) if abs_path else '/'.join(stack)


class QueueWithMax(object):
  """Deque class with max operator."""

  def __init__(self):
    self._queue = collections.deque()
    self._max_queue = collections.deque()

  def enqueue(self, val):
    self._queue.append(val)
    while self._max_queue and self._max_queue[-1] < val:
      self._max_queue.pop()
    self._max_queue.append(val)
    return

  def enqueue_multiple(self, a):
    for val in a:
      self.enqueue(val)
    return

  def dequeue(self):
    val = self._queue.popleft()
    if self._max_queue[0] == val:
      self._max_queue.popleft()
    return val

  def max(self):
    return self._max_queue[0]
