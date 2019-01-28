"""Heap o' trouble!"""
import heapq
import collections

def merge_sorted_lists(a):
  """Merge already sorted lists into one complete list.

  Time complexity: O(N log k), where k is the number of lists
  Space complexith: O(k)

  Args:
    a: List of lists

  Returns:
    Sorted list
  """

  HeapVal = collections.namedtuple('HeapVal', ['value', 'index'])
  iters = [iter(slist) for slist in a]
  heap = [HeapVal(next(iters[i], None), i) for i in range(len(a))]
  heapq.heapify(heap)
  ret = []
  while heap:
    hv = heapq.heappop(heap)
    if hv.value is None:
      continue
    ret.append(hv.value)
    next_val = next(iters[hv.index], None)
    if next_val is not None:
      heapq.heappush(heap, HeapVal(next_val, hv.index))
  return ret


class ContainerWithMedian(object):
  """Data container with O(1) access to median."""

  def __init__(self):
    self.min_heap = []
    self.max_heap = []

  def append(self, value):
    """Add value in O(log N) time."""

    # Push into min_heap and then back to max_heap to ensure entries in
    # max_heap less than those in min_heap
    heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -value)) 
    # Ensure min_heap not larger than max_heap
    if len(self.min_heap) > len(self.max_heap):
      heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

  def median(self):
    """Returns median of current data in O(1) time."""

    # max_heap always carries odd value, else take average if equal length
    return (
        -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else
        0.5 * -self.max_heap[0] + 0.5 * self.min_heap[0])

