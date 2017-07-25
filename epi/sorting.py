import heapq

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
    int number of max overlaps """
  max_overlap = 0
  live_events = []
  for event in events:
    # Remove all events from heap that end before this event starts
    while live_events and event.start > live_events[0]:
      heapq.heappop(live_events)
    heapq.heappush(live_events, event.end)
    max_overlap = max(max_overlap, len(live_events))
  return max_overlap
