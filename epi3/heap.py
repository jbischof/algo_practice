import heapq

def merge_sorted_arrays(*arrays):
    """
    Merge sorted arrays in single globally sorted array with heaps.

    Time: O(n log k), Space: O(k), where k is the number of arrays.
    """

    heap = []
    res = []
    for array in arrays:
        # Seed heap with iterators
        it = iter(array)
        first = next(it, None)
        if first is not None:
            heapq.heappush(heap, (first, it))
    while heap:
        first, it = heapq.heappop(heap)
        res.append(first)
        second = next(it, None)
        if second is not None:
            heapq.heappush(heap, (second, it))
    return res


def streaming_median(stream):
    """
    Calculate running median of an online stream of data. Need to return
    median after process each data point.

    If just wanted median of static array, could use quick select to find it
    in O(N) time. If want running median, more complicated.

    Idea: Median is the midpoint of the data. If maintain two heaps, one a min
    heap and one a max heap would always have access to those middle points.
    Then if N is odd you take the root of the larger one and if it is even you
    average the roots. When you get a new data point you compare it to the roots
    of the two heaps to decide where it goes and pop as necessary.
    Time: O(N log N), Space: O(N)

    [1, 0, 3, 5, 2, 0, 1]
    small, big, new_median
    1: [], [1], 1
    0: [0], [1], 0.5
    3: [0], [1, 3], 1
    5: [0, -1], [3, 5], 2
    2: [0, -1], [2, 3, 5], 2
    0: [0, 0, -1], [2, 3, 5], 1.5
    1: [0, 0, -1], [1, 2, 3, 5], 1
    """

    big_heap = []
    small_heap = []
    running_medians = []
    first = next(stream)
    running_medians.append(first)
    heapq.heappush(big_heap, first)
    for item in stream:
        # Push pop on bigger heap to keep sizes aligned
        if len(small_heap) >= len(big_heap):
            item = heapq.heappushpop(small_heap, item * -1)
            heapq.heappush(big_heap, item * -1)
        else:
            item = heapq.heappushpop(big_heap, item)
            heapq.heappush(small_heap, item * -1)

        if len(small_heap) == len(big_heap):
            running_medians.append(-0.5 * small_heap[0] + 0.5 * big_heap[0])
        else:
            # Big heap always the bigger one
            running_medians.append(big_heap[0])

    return running_medians

