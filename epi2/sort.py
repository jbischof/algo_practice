"""Sorting problems."""
import collections
import heapq

def array_intersect(a, b):
  """Return the intersection of two sorted arrays.
  
  Time: O(len(a) + len(b))
  Space: O(1)
  """
  
  it1, it2 = iter(a), iter(b)
  val1, val2 = next(it1, None), next(it2, None)
  res = []

  while val1 and val2:
    if val1 == val2:
      if not res or res[-1] < val1:
        res.append(val1)
      val1 = next(it1, None)
      val2 = next(it2, None)
    elif val1 < val2:
      val1 = next(it1, None)
    else:
      val2 = next(it2, None)

  return res


def merge_sorted_arrays(a, b):
  """In-place merge of sorted arrays into array `a`.
  
  Time: O(len(a) + len(b))
  Space: O(1)
  """

  # Ensure first array has enough space for all entries
  i, j = len(a) - 1, len(b) - 1
  a.extend([None] * len(b))
  pos = len(a) - 1

  while pos >= 0:
    if j < 0 or (i >= 0 and a[i] >= b[j]):
      a[pos] = a[i]
      i -= 1
    else:
      a[pos] = b[j]
      j -= 1
    pos -= 1
  return

  
Event = collections.namedtuple('Event', ['start', 'end'])

def max_event_overlap(events):
  """Determine maximum number of events that overlap.

  Time: O(N)
  Space: O(N)
  
  Args:
    events: Iterable of Event objects.
  """

  heap = []
  max_overlap = 0

  for event in sorted(events, key=lambda x: x.start):
    while heap and heap[0] <= event.start:
      heapq.heappop(heap)
    heapq.heappush(heap, event.end)
    max_overlap = max(max_overlap, len(heap))

  return max_overlap


def merge_disjoint_events(events, new_event):
  """Merge sorted array of disjoint intervals with new interval.
  
  Time: O(N)
  Space: O(N)
  
  Args:
    events: Iterable of Event objects.
    new_event: Event object

  Returns: Array of new events
  """
  
  res = []
  it = iter(events)
  next_event = next(it, None)
  joined_event = new_event
  while next_event and next_event.end < new_event.start:
    # Push through events that end before new one to res
    res.append(next_event)
    next_event = next(it, None)
  while next_event and next_event.start < new_event.end:
    joined_event = Event(min(joined_event.start, next_event.start),
                         max(joined_event.end, next_event.end))
    next_event = next(it, None)
  res.append(joined_event)
  while next_event:
    # Remaining events start after this event ends
    res.append(next_event)
    next_event = next(it, None)
  return res

