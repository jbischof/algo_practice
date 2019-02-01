"""Hashing problems."""
import collections
import linked_list as ll

def is_perm_palindrome(s):
  """Returns True is string can be permuted to a palindrome."""

  counter = collections.Counter(s)
  num_odds = 0

  for count in counter.values():
    if count & 1:
      num_odds += 1
    if num_odds > 1:
      return False

  return True


LRUItem = collections.namedtuple('LRUItem', ['key', 'value'])

class LRUCache(object):
  def __init__(self, capacity=10):
    self.capacity = capacity
    self.dll = ll.DoublyLinkedList()
    self.dict = {}

  def lookup(self, key):
    if key in self.dict:
      return True, self.dict[key].data.value
    else:
      return False, None

  def insert(self, key, value):
    if key in self.dict:
      # Data already in LRU: don't update but move to front of line
      node = self.dict[key]
      self.dll.delete(node)
      self.dll.insert_at_head(node)
      return
    if len(self.dict) >= self.capacity:
      # Evict LRU node if at capacity
      lru_node = self.dll.tail
      self.dll.delete(lru_node)
      self.dict.pop(lru_node.data.key)
    # Insert new node at head of queue
    node = ll.Node(LRUItem(key=key, value=value))
    self.dict[key] = node
    self.dll.insert_at_head(node)
    return

  def keys(self):
    return [x.key for x in self.dll.values()]

  def erase(self, key):
    if key not in self.dict:
      raise KeyError('Key not in LRU')
    # Remove entry
    node = self.dict[key]
    self.dict.pop(key)
    self.dll.delete(node)
    return


def find_closest_repeat(a):
  """Return closest repeated word in array of strings.
  
  Time: O(n)
  Space: O(m), where m is number of unique strings.
  """

  worst_repeat, worst_dist = None, len(a) + 1
  wdict = {}
  for i, s in enumerate(a):
    if s not in wdict:
      wdict[s] = i
    else:
      dist = i - wdict[s]  
      wdict[s] = i
      if dist < worst_dist:
        worst_repeat = s 
        worst_dist = dist
  return worst_repeat


def find_keyword_span(a, b):
  """Find smallest subarray in a that contains keywords in set b.
  
  Args:
    a: List of strings.
    b: Set of string to find in subarray.

  Returns:
    Tuple of start, end positions of smallest subarray with set.
  """

  words_to_find = set(b)
  words_left = set(b)
  word_pos = collections.deque()
  left, right = None, None
  best_subset = None

  for pos, word in enumerate(a):
    if word not in words_to_find:
      continue
    word_pos.append(pos)
    words_left.discard(word)
    if not words_left:
      # Complete set obtained: try to shrink
      while len(word_pos) > 1 and a[word_pos[0]] == word:
        # Try to remove redundant words from front
        word_pos.popleft()
      left, right = word_pos[0], word_pos[-1]
      if not best_subset or (right - left + 1) < best_subset[0]:
        best_subset = (right - left + 1, left, right)

  return best_subset[1:]
