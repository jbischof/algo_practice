import heapq
import collections

def merge_sorted_arrays(a, b):
  """ Merge contents of sorted array 'b' into sorted array 'a' without creating
  new array. Operation is in-place. """
  n, m = len(a), len(b)
  a.extend([None] * m)
  a_idx, b_idx, write_idx = n - 1, m - 1, n + m - 1
  while a_idx >= 0 and b_idx >= 0:
    if a[a_idx] > b[b_idx]:
      a[write_idx] = a[a_idx]
      a_idx -= 1
      write_idx -= 1
    else:
      a[write_idx] = b[b_idx]
      b_idx -= 1
      write_idx -= 1
  if b_idx > 0:
    a[0 : b_idx + 1] = b[0 : b_idx + 1]

class Event():
  def __init__(self, start, end):
    if not start <= end:
      raise ValueError("start must be less than or equal to end.")
    self.start = start
    self.end = end

def event_max_overlap(events):
  """ Compute maximum number of events that overlap in list.
  Args:
    events: List of Event objects
  Returns:
    int number of max overlaps
  Time complexity: O(n log n)
  Space complexity: O(n) """
  max_overlap = 0
  live_events = []
  for event in events:
    # Remove all events from heap that end before this event starts
    while live_events and event.start > live_events[0]:
      heapq.heappop(live_events)
    heapq.heappush(live_events, event.end)
    max_overlap = max(max_overlap, len(live_events))
  return max_overlap

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

def partition_object_array(a, key):
  """ Partition array of objects using key
  Args:
    a: Array of objects
    key: member variable of object to use for partition
  Returns:
    None. Partition is in-place.
  Time complexity: O(N)
  Space complexity: O(1) """
  # Make hash table counting number of objects of each key value
  key_count = collections.Counter([getattr(obj, key) for obj in a])
  # Create mapping of key to first index in partitioned array
  index = 0
  key_index = {}
  for key_val, count in key_count.iteritems():
    key_index[key_val] = index
    index += count
  # Iterate through key positions and swap objects into place
  while key_index:
    # Get first key in key_index with some objects not in partitioned position
    next_key = next(iter(key_index))
    # Determine which position key should be in
    next_pos = key_index[next_key]
    # Determine what key currently in that position
    swap_key = getattr(a[next_pos], key)
    # Determine which position that key should be moved to
    swap_pos = key_index[swap_key]
    # Swap two objects
    a[next_pos], a[swap_pos] = a[swap_pos], a[next_pos]
    # Mark swapped item as in place
    key_count[swap_key] -= 1
    if key_count[swap_key]:
      key_index[swap_key] += 1
    else:
      del key_index[swap_key]
