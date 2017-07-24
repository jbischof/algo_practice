import collections
import Queue

def is_palindrome_permuted(s):
  """ Checks if string s can be converted to a palindrome under permutation. """
  char_dict = collections.Counter()
  for char in s:
    char_dict[char] += 1
  # Palindrome requires no more than one char has odd number of occurrences
  num_odd = 0
  for val in char_dict.values():
    if val % 2 != 0:
      num_odd += 1
  if num_odd > 1:
    return False
  return True

def find_nearest_repeat(a):
  """ Find the two duplicates in a that are closest together
  Args:
    a: A list with hashable items
  Returns:
    Tuple with indicies of repeated elements """
  # Make hashmap of items and min distances
  dist_dict = {}
  for i, item in enumerate(a):
    if item in dist_dict:
      last_index, min_dist, _ = dist_dict[item]
      if i - last_index < min_dist:
        dist_dict[item] = (i, i - last_index, (last_index, i))
    else:
      dist_dict[item] = (i, float('Inf'), None)
  # Find minimum entry in dict
  best_dist = float('Inf')
  ret = (None, None)
  for metadata in dist_dict.values():
    _, min_dist, indicies = metadata
    if min_dist < best_dist:
      best_dist = min_dist
      ret = indicies
  return ret

def find_smallest_match_subarray(a, b):
  """ Find the smallest subarray in 'a' that contains all elements in 
  subarray 'b'. In the case of a tie, returns first subset
  Time complexity: O(N)
  Space Complexity: O(N)
  Args:
    a: An array
    b: An array with elements also in b
  Returns:
    Tuple with (start, stop) indicies of best subarray
  """
  b = set(b)
  b_record = set(b)
  best_subset = ()
  start, end = None, None
  # Positions of items in set(b)
  position_queue = Queue.Queue(len(a)) 
  for i, val in enumerate(a):
    if val not in b:
      continue
    position_queue.put(i)
    if val in b_record:
      b_record.remove(val)
    if start is None:
      start = i
    if not len(b_record):
      # All items have been found!
      if end is None:
        # This is the first time
        end = i
        best_subset = (end - start + 1, start, end)
      else:
        end = i
        # This is not the first time, see if can move start forward
        while a[start] == val:
          start = position_queue.get()
          # See if can update best_subset
          if end - start + 1 < best_subset[0]:
            best_subset = (end - start + 1, start, end)
  return best_subset[1:]
