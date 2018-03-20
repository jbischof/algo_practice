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

