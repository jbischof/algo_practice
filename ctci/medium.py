"""Medium difficulty problems, as defined by book."""

import collections
import heapq

def find_min_distance(a1, a2):
  """Find the smallest pairwise distance between items in two arrays.
  
  Time complexity: O(N_1(log N_1) + N_2(log N_2))
  Space complexity: O(1)
  """

  a1.sort()
  a2.sort()
  min_diff = float('inf')
  a1_pos, a2_pos = 0, 0
  while a1_pos + a2_pos <= len(a1) + len(a2) - 2:
    min_diff = min(min_diff, abs(a1[a1_pos] - a2[a2_pos]))
    # Try to decrease min by augmenting lower number
    # No need to increase list with remaining numbers if already greater
    if a1[a1_pos] <= a2[a2_pos] and a1_pos < len(a1) - 1:
      a1_pos += 1
    elif a2[a2_pos] <= a1[a1_pos] and a2_pos < len(a2) - 1:
      a2_pos += 1
    else:
      break
  return min_diff


Person = collections.namedtuple('Person', ('birth_year', 'death_year'))


def max_population_year(persons):
  """Determine year when maximum number of people alive.

  Args:
    person: An iterable of Person tuples.

  Returns:
    Int.

  Time complexity: O(N log N)
  Space complexity: O(N)
  """

  persons.sort(key=lambda x: x.birth_year)
  heap = []
  bestYear = persons[0].birth_year
  bestNum = 1
  for person in persons:
    # Figure out how many alive after birth
    while heap and heap[0] < person.birth_year:
      heapq.heappop(heap)
    heapq.heappush(heap, person.death_year)
    # Replace bestYear if better than previous best
    if len(heap) > bestNum:
      bestYear, bestNum = person.birth_year, len(heap)
  return bestYear
    

def subsort_indices(a):
  """Find subarray to sort that makes entire array stored.

  First identify minimal subarray, defined as complement of increasing sequence
  from the left and decreasing from the right. Then check indices to left and
  make sure all less than min(minimal, right) and indices to the right and make
  sure all greater than max(left, minimal).

  Time complexity: O(N)
  Space complexity: O(1)

  Args:
    a: Array of ints
  
  Returns:
    Tuple with indices of subarray. Returns None if array already sorted.
  """

  # Find left side of minimal subarray
  left_pos = 0
  for i in xrange(1, len(a)):
    if a[i] >= a[left_pos]:
      left_pos += 1
    else:
      break

  # Done if entire array sorted
  if left_pos >= len(a) - 1:
    return None

  # Find right side of subarray
  right_pos = len(a) - 1
  for i in xrange(len(a) - 2, left_pos, -1):
    if a[i] <= a[right_pos]:
      right_pos -= 1
    else:
      break

  # Extend subarray to the left if anything bigger there
  min_right = min(a[left_pos: ])
  for i in xrange(left_pos - 1, -1, -1):
    if a[i] >= min_right:
      left_pos = i
    else:
      break
  
  # Extend subarray to the right if anything smaller there
  max_left = max(a[ :right_pos + 1])
  for i in xrange(right_pos + 1, len(a)):
    if a[i] <= max_left:
      right_pos = i
    else:
      break

  return (left_pos, right_pos)


