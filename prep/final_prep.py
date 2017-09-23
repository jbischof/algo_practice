"""Problems where the data structure or algorithm is unspecified.

This mimics the actual interview conditions.
"""
import heapq
import imp
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
  counter = 0
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
