"""Problems where the data structure or algorithm is unspecified.

This mimics the actual interview conditions.
"""
import heapq
import imp
import collections
import sys
sys.path.append('../epi/')
import binary_tree as bt
import bst
import string
import copy


def longest_twochar_substr(a):
  """Find the longest substring with at most two unique characters.
  
  Time complexity: O(N)
  Space complexity: O(N)
  Args:
    a: string
  Returns:
    substring
  """

  best_substr = [0, 0]
  substr = [0, 0]
  pos = 0
  # Dictionary mapping unique chars to last seen position
  charpos = {}
  while pos < len(a):
    char = a[pos]
    charpos[char] = pos 
    if len(charpos) <= 2:
      substr[1] = pos
      pos += 1
      continue
    # Record current substring if the best
    if substr[1] - substr[0] > best_substr[1] - best_substr[0]:
      best_substr = substr
    # Extract char with lowest count
    low_key = next(iter(charpos))
    low_val = charpos[low_key]
    for key, value in charpos.iteritems():
      if value < low_val:
        low_key = key
        low_val = value
    charpos.pop(low_key)
    substr = [low_val + 1, pos] 
  return a[best_substr[0] : (best_substr[1] + 1)] 


def longest_Mchar_substr(a, m):
  """Find the longest substring with at most M unique characters.
  
  Time complexity: O(N * log M)
  Space complexity: O(N + M)
  Args:
    a: string
    m: Number of unique characters allowed in substring
  Returns:
    substring
  """

  best_substr = [0, 0]
  substr = [0, 0]
  pos = 0
  # Dictionary mapping unique chars to last seen position
  charpos = {}
  # BST holds sorted version of dictionary
  charpos_bst = bst.BST()
  while pos < len(a):
    char = a[pos]
    if char in charpos:
      charpos_bst.remove_value((charpos[char], char))
    charpos_bst.insert(bt.Node((pos, char)))
    charpos[char] = pos 
    if len(charpos) <= m:
      substr[1] = pos
      pos += 1
      continue
    # Record current substring if the best
    if substr[1] - substr[0] > best_substr[1] - best_substr[0]:
      best_substr = substr
    # Extract char with lowest count
    low_val, low_key = charpos_bst.k_smallest(1)[0]
    charpos_bst.remove_value((low_val, low_key))
    charpos.pop(low_key)
    substr = [low_val + 1, pos] 
  return a[best_substr[0] : (best_substr[1] + 1)] 


def is_deck_valid(a):
  """Check if array of ints can be partitioned into consecutive triplets.

  Array represents `deck` of numbered cards. Duplicates are possible.

  Time complexity: O(N log N). Time dominated by sorting the keys.
  Space complexity: O(N). Space needed to create counter and key list.

  Args:
    a: An iterable of ints
  Returns:
    Bool.
  """

  if len(a) % 3 != 0:
    return False

  counter = collections.Counter(a)
  # Get sorted keys from collection
  sort_counts = [[key, counter[key]] for key in sorted(counter.keys())]
  index = 0
  max_index = len(sort_counts) - 3 
  while index <= max_index:
    c0, c1, c2 = (
        sort_counts[index][0],
        sort_counts[index + 1][0], 
        sort_counts[index + 2][0])
    # Check that three keys consecutive and all have counts
    if (
        c1 - c0 == 1 and sort_counts[index + 1][1] and
        c2 - c0 == 2 and sort_counts[index + 2][1]):
      sort_counts[index][1] -= 1
      sort_counts[index + 1][1] -= 1
      sort_counts[index + 2][1] -= 1
      while index <= max_index and not sort_counts[index][1]:
        index += 1
    else:
      return False
  # Make sure nothing left at end of list 
  if sort_counts[max_index + 1][1] or sort_counts[max_index + 2][1]:
    return False
  return True


def is_tree(adj_list):
  """Returns true if graph is a DAG (tree).

  Time complexity: O(|V| + |E|) for DFS and recording all nodes
  Space complexity: O(|V|) for node sets

  Args:
    adj_list: A dictionary mapping node name to set of connected nodes.
  Returns:
    Bool.
  """

  # Determine set of candidates for root: parent, never a child
  # Value `1` means candidate for root; value `0` means blacklisted
  only_parents = {}
  # Make record of all nodes seen
  all_nodes = set()
  for node, edges in adj_list.iteritems():
    all_nodes.add(node)
    if node not in only_parents:
      only_parents[node] = 1
    for edge in edges:
      only_parents[edge] = 0

  edge_cands = [node for node, val in only_parents.iteritems() if val == 1]
  if len(edge_cands) != 1:
    return False

  # Conduct DFS starting from candidate root
  root = edge_cands.pop()
  visited = set()
  if not is_tree_helper(root, adj_list, visited):
    return False
  # Make sure all nodes visited
  if all_nodes - visited:
    return False
  return True 


def is_tree_helper(current, adj_list, visited):
  """Recursive function to traverse graph checking if tree.

  Args:
    current: Name of node being visited
    adj_list: See `is_root`
    visited: Set of nodes already visited
  Returns:
    Bool. False if any node visited twice, True otherwise.
  """

  if current in visited:
    return False
  visited.add(current)
  for edge in adj_list[current]:
    if not is_tree_helper(edge, adj_list, visited):
      return False
  return True


def is_subset_sum(a, k, offset=0):
  """Determine if any subset of positive int array sums to k.

  Time complexity: O(2^N), size of power set
  Space complexity: O(N) from maximum recursion depth

  Args:
    a: List of positive integers.
    k: Integer.

  Returns:
    Bool.
  """

  # Base cases:
  if k == 0:  # Hit target
    return True
  if k < 0:  # Overshot
    return False
  if offset >= len(a):  # Nothing left with k > 0
    return False

  # Recursive case: k > 0 and items left
  return ( 
      is_subset_sum(a, k, offset + 1) or 
      is_subset_sum(a, k - a[offset], offset + 1))


class Partition(object):
  def __init__(self, end=None, total=0):
    self.end = end
    self.total = total

  def __eq__(self, other):
    return (self.end, self.total) == (other.end, other.total)

  def __ne__(self, other):
    return not self.__eq__(other)


def _partition_array_weight(a, k, w):
  """Divide array into `k` partitions, each with total sum < `w`

  Time complexity: O(N)
  Space complexity: O(1)

  Args:
    a: List of ints
    k: Number of partitions
    w: Max sum in each partition
  
  Returns:
    List of partition objects or None if partition not possible
  """

  ret = [Partition() for _ in range(k)]
  curr = 0
  for i in range(len(a)):
    if ret[curr].total + a[i] <= w:
      ret[curr].end = i
      ret[curr].total += a[i]
    elif curr >= k - 1:
      return None
    else:
      # Start new partition
      curr += 1
      ret[curr].end = i
      ret[curr].total = a[i]
  
  return ret


def min_cargo_capacity(a, k):
  """Find the minimum cargo capacity needed using binary search.

  Time complexity: O(N * log(sum(a))) ###CHECK THIS
  Space complexity: O(k)

  Returns:
    Min weight needed to ship cargo in k shipments.
  """

  L, U = max(a), sum(a)
  best_ans = _partition_array_weight(a, k, U)
  while L <= U:
    M = (L + U) // 2
    ans = _partition_array_weight(a, k, M)
    if ans:
      best_ans = ans
      U = M - 1
    else:
      L = M + 1

  return max([x.total for x in best_ans])


def multinomial_rng(probs, unif):
  """Produce sample from multinomial given unif draw.

  Args:
    probs: Vector of probabilities across k classes that sum to one.
    unif: Uniform random number in [0, 1]

  Returns:
    Int from 0 to k-1.
  """

  cum = 0
  cum_dist = []
  for k in range(len(probs)):
    cum += probs[k] 
    cum_dist.append(cum)
  
  ret = 0
  L, U = 0, len(cum_dist) - 1
  while L <= U:
    M = (L + U) // 2
    if unif < cum_dist[M]:
      ret = M
      U = M - 1
    else:
      L = M + 1

  return ret


class LastUniqueInt(object):
  def __init__(self):
    self.counter = collections.Counter() 
    self.stack = []
    self.last_unique = None

  def update_last_unique(self, i):
    """Update the last unique int seen so far.
    
    Args:
      i: Next int seen.

    Returns:
      Last unique int seen.
    """

    if i in self.counter:
      self.counter[i] += 1
      if i == self.last_unique:
        while self.counter[self.stack[-1]] > 1:
          self.stack.pop()
        self.last_unique = self.stack.pop()
    else:
      self.counter[i] += 1
      self.stack.append(i)
      self.last_unique = i

    return self.last_unique


def is_ul_pair(first, second):
  """Check if two strings are upper and lower case swaps from each other."""

  return first == string.swapcase(second) 


def remove_char_case_pairs(b):
  """Remove all pairs of same char but different case from bytearray.

  Args:
    b: bytearray

  Returns:
    Lenth of new bytearray
  """

  read_pos, write_pos = 0, -1
  last_pos = len(b) - 1
  while read_pos <= last_pos:
    if (read_pos < last_pos and 
        is_ul_pair(chr(b[read_pos]), chr(b[read_pos + 1]))):
      # Next two chars are match; skip ahead
      read_pos += 2
    elif write_pos >= 0 and is_ul_pair(chr(b[read_pos]), chr(b[write_pos])):
      # Take back last write and don't write this one either
      write_pos -= 1
      read_pos += 1
    else:
      # Legal char
      write_pos += 1
      b[write_pos] = b[read_pos]
      read_pos += 1
      
  return None if write_pos < 0 else write_pos + 1


class NaryNode(object):
  def __init__(self, name):
    self.name = name
    self.edges = []

class NaryEdge(object):
  def __init__(self, to=None, dist=0):
    self.to = to 
    self.dist = dist

def furthest_leaf_dist(root):
  """Find the distance to the furthest leaf in an n-ary tree.

  Args:
    root: Object of type NaryNode

  Returns:
    Distance to furthest node.
  """

  longest_dist = 0
  queue = collections.deque([root])
  dists = {root.name: 0}

  while queue:
    curr = queue.popleft()
    for edge in curr.edges:
      dists[edge.to.name] = dists[curr.name] + edge.dist
      longest_dist = max(longest_dist, dists[edge.to.name])
      queue.append(edge.to)

  return longest_dist


def forest_after_delete(root, to_delete):
  """Return list of subtrees remaining after nodes in `to_delete` removed.

  Args:
    root: Object of class bt.Node
    to_delete: Set of values to be deleted

  Returns:
    List of root nodes of resulting forest.
  """

  ret = []
  if root.value not in to_delete:
    ret.append(root)
  fad_helper(root, to_delete, ret)
  return ret


def fad_helper(root, to_delete, ret):
  if root is None:
    return
  if root.value in to_delete:
    # Add children to ret if not also deleted
    if root.left and root.left.value not in to_delete:
      ret.append(root.left)
    if root.right and root.right.value not in to_delete:
      ret.append(root.right)
  fad_helper(root.left, to_delete, ret)
  fad_helper(root.right, to_delete, ret)
  # Clean up child pointers
  if root.left and root.left.value in to_delete:
    root.left = None 
  if root.right and root.right.value in to_delete:
    root.right = None 
  return


class Interval(object):
  def __init__(self, start, end, events=None):
    self.events = events or set()
    self.start = start
    self.end = end

  def to_tuple(self):
    return (self.start, self.end, self.events)

  def __eq__(self, other):
    return self.to_tuple() == other.to_tuple()

  def __ne__(self, other):
    return not self.__eq__(other)


def distinct_overlapping_intervals(intervals):
  """Computes set of intervals with each unique set of events active.

  Args:
    Iterable of Interval objects giving set of events. Each interval should
        have only one active event.

  Returns:
    List of Interval objects with each unique set of events active.
  """

  # Divide intervals into start and end events
  events = [(x.start, True, next(iter(x.events))) for x in intervals]
  events.extend([(x.end, False, next(iter(x.events))) for x in intervals])
  events.sort()
  ret = []
  active_events = set()
  # Time of last event change
  last_time = None
  for time, is_start, event in events:
    if is_start:
      if active_events and time - last_time > 0:
        ret.append(Interval(last_time, time, copy.deepcopy(active_events)))
      active_events.add(event)
    else:  # Event is ending
      if time - last_time > 0:
        ret.append(Interval(last_time, time, copy.deepcopy(active_events)))
      active_events.discard(event)
    last_time = time

  return ret

