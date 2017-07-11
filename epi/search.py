import bisect

def find_first(a, x):
  """ Find *first* occurrence of x in array. 
  Only difference from binary search that condition is to find x in first
  position or a lower value in the previous position
  Time: O(log n) """
  low, high = 0, len(a) - 1
  while low <= high:
    index = (low + high) // 2
    # Move higher index down if value greater than x or still stuck within the
    # x values
    if a[index] > x or (index > 0 and a[index] == x and a[index - 1] == x):
      high = index - 1
    # Move lower up if value less than x
    elif a[index] < x:
      low = index + 1
    # Otherwise you found it!
    else:
      return index
  return -1

def find_min_cyclic_sorted(a):
  """ Find the minimum value of a cyclically sorted array.
  Assume no repeated values in array.
  E.g., if a = [9, 6, 5, 0, 2, 3], returns 3
  Algorithm uses bisection and is O(N) complexity """
  low, high = 0, len(a) - 1
  max_value = a[-1]
  while low < high:
    index = (low + high) // 2
    if a[index] < max_value:
      high = index
    else:
      low = index + 1
  return low 

def int_sqrt(x):
  """ Returns the largest integer i such that i^2 < x.
  Time complexity: O(log n) """
  low, high = 1, x
  while low <= high:
    i = (low + high) // 2
    if i*i > x:
      high = i - 1
    else:
      low = i + 1
  return low - 1

def search_2d(a, x):
  """ Search a two-dimensional sorted array for element x.
  2d sorted means that all rows and columns are non-decreasing
  Time complexity: O(n + m) """
  nrow = len(a)
  ncol = len(a[0])
  i, j = 0, ncol - 1
  # End when go outside of indices
  while i >= 0 and i < nrow and j >= 0 and j < ncol:
    if a[i][j] == x:
      return True
    elif a[i][j] > x:
      j -= 1
    else:
      i += 1
  return False

def partition(a, low, high):
  """ Partition array using pivot element in last position of window.
  Time complexity: O(high - low).
  Args:
    a: array with length >= high
    low, high: beginning and ending positions of array to partition with pivot
  Returns:
    New position of pivot. Array changed in-place.
  """
  pivot_pos = high
  pivot_val = a[pivot_pos]
  i = 0
  swap = pivot_pos - 1
  while i < pivot_pos:
    if a[i] < pivot_val:
      i += 1
    else:
      a[i], a[swap] = a[swap], a[i]
      a[pivot_pos], a[swap] = a[swap], a[pivot_pos]
      pivot_pos -= 1
      swap -= 1
  return pivot_pos

def find_kth_smallest(a, k):
  """ Find kth smallest element in array. Implements quickselect algorithm.
  Args:
    a: array with length >= k
    k: index of element in sorted array
  Returns:
    kth smallest item 
  Time complexity: O(n) """
  k_pos = k - 1
  low, high = 0, len(a) - 1
  while low < high:
    pivot_pos = partition(a, low, high)
    if pivot_pos == k_pos:
      return a[pivot_pos]
    elif pivot_pos > k_pos:
      high = pivot_pos - 1
    else:
      low = pivot_pos + 1
  return a[low]

def find_missing_8bit_int(a):
  """ Finds missing 8-bit integer in array a out of 256 possibilities
  Builds a smaller index of possible 4-bit prefixes to narrow the search
  This could have application when looking for missing 32- or 64-bit ints
  where enumerating the possibilties is infeasible.
  Args:
    a: An array of 8-bit positive integers (can use regular ints < 256)
  Returns:
    A 8-bit integer not present in a
  """
  if len(a) >= 256:
    raise ValueError("Array not missing any ints")
  # 16 ints are expected for each of the 16 unique prefixes
  NUM_INTS = 16
  prefix_counts = [0] * 16
  for aint in a:
    prefix = aint >> 4
    prefix_counts[prefix] += 1
  # Choose prefix with count < 16
  for i, count in enumerate(prefix_counts):
    if count < NUM_INTS:
      chosen_prefix = i
      break
  # Build array of expected ints
  expect_array = [0] * 16
  for aint in a:
    if aint >> 4 == chosen_prefix:
      expect_array[aint & 0b1111] = 1
  # Return first missing int
  for suffix, count in enumerate(expect_array):
    if not count:
      return chosen_prefix << 4 | suffix

