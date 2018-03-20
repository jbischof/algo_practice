"""Searching and sorting problems."""

def merge_sorted_arrays(a, b):
  """Merge two sorted arrays into the first.
  
  Time complexity: O(N)
  Space complexity: O(1)
  """
  
  a_pos, b_pos = len(a) - 1, len(b) - 1
  # Add enough capacity at end of `a` to store values in `b`
  a.extend([None] * len(b))
  # Fill `a` from the back with largest entries from each
  fill_pos = len(a) - 1
  while fill_pos >= 0 and b_pos >= 0:
    # If all elements in `b` moved, remaining `a` already in correct position
    if a_pos < 0 or a[a_pos] < b[b_pos]:
      # Pull from `b` if all `a` elements moved or next `a` element smaller 
      a[fill_pos] = b[b_pos]
      b_pos -= 1
    else:
      # Pull from `a` otherwise
      a[fill_pos] = a[a_pos]
      a_pos -= 1
    fill_pos -= 1


def binary_search_rotated(a, k):
  """Search for item in rotated array.
  
  Deal with three cases:
    - Subarray not rotated
    - Subarray rotated and mid is in the front of the original
    - Subarray rotated and mid is in the back of the original
  """
  low, high = 0, len(a) - 1
  while low <= high:
    mid = (low + high) // 2
    if k == a[mid]:
      return mid
    if a[mid] <= a[high] and a[mid] >= a[low]:
      # In regular BS land
      if k < a[mid]:
        high = mid - 1
      else:
        low = mid + 1
    elif a[mid] < a[high] and a[mid] < a[low]:
      # Mid in front of original array
      if k > a[mid]:
        if k <= a[high]:
          low = mid + 1
        else:
          high = mid - 1
      else:
        high = mid - 1
    else:
      # Mid in back of original array
      if k < a[mid]:
        if k <= a[low]:
          low = mid + 1
        else: 
          high = mid - 1
      else:
        low = mid + 1
  return None 
