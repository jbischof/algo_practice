import heapq

def merge_sorted_arrays(array_list):
  """ Merges a list of sorted arrays into a single sorted array.
  If input is M lists of total length N, algorithm takes O(N log(M)) time
  and O(M) storage.
  Note: This functionality is already available with heapq.merge.
  Args:
    array_list: A list of arrays
  Returns:
    Single array
  """
  # Create a heap structure to store arrays
  heap = []
  # Create list of iterators to move over arrays
  iters = [iter(a) for a in array_list]
  # Push each list's min element to heap with index marker
  for i, iterator in enumerate(iters):
    next_item = next(iterator, None)
    if next_item is not None:
      heapq.heappush(heap, (next_item, i))
  ret = []
  while heap:
    min_value, heap_index = heapq.heappop(heap)
    ret.append(min_value)
    next_item = next(iters[heap_index], None)
    if next_item is not None:
      heapq.heappush(heap, (next_item, heap_index))
  return ret

def sort_k_sorted(a, k=1):
  """ Sort an array where each item no more than k positions away from correct
  location.
  Time complexity: O(n log k)
  Space complexity: O(k) """
  # Window size
  size = k + 1
  # Initialize heap
  heap = a[0 : min(size, len(a))]
  heapq.heapify(heap)
  for i in range(len(a)):
    a[i] = heapq.heappop(heap)
    if (i + size) < len(a):
      heapq.heappush(heap, a[i + size])
  return a

def k_smallest(a, k):
  """ Find the k smallest values in a
  Note: This functionality is already available in heapq.ksmallest
  Time complexity: O(n log k)
  Space complexity: O(k) """
  # Set ceiling for k at length of array
  k = min(k, len(a))
  # Flip sign on values of a to get max heap
  a = [x * -1 for x in a]
  # Initialize heap
  heap = a[ : k]
  heapq.heapify(heap)
  for i in range(k, len(a)):
    if a[i] > heap[0]:
      heapq.heapreplace(heap, a[i])
  # Extract sorted items from heap
  ret = [0] * k
  # Have to extract from max heap in reverse order to get smallest first
  for i in range(k - 1, -1, -1):
    ret[i] = -1 * heapq.heappop(heap)
  return ret

