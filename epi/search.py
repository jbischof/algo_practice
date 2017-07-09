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
