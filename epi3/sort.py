"""Sorted problems."""
import heapq

def list_intersection(a, b):
    """
    Compute the intersection of two sorted lists.

    Args:
        a, b: A list

    Brute force: Puts the lists into sets and compute the intersection.
    Time: O(N + M), Space: O(N + M)

    Idea: Maintain a pointer traversing each list and advance the pointer with
    a lower value in that position. If the values are the same, emit to result
    list. Time: O(N + M), Space: O(1)

         0, 1, 2, 3, 4, 5
    a = [1, 3, 5, 5, 7, 9]
    b = [2, 2, 3, 3, 5, 8]
    it_a, it_b, res
    0, 0, []
    1, 0, []
    1, 1, []
    1, 2, []
    2, 3, [3]
    2, 4, [3]
    3, 5, [3, 5]
    4, 5, [3, 5]
    5, 5, [3, 5]
    5, 6, [3, 5]
    """

    it_a, it_b = 0, 0
    res = []
    while it_a < len(a) and it_b < len(b):
        if a[it_a] < b[it_b]:
            it_a += 1
        elif a[it_a] == b[it_b]:
            if len(res) == 0 or res[-1] != a[it_b]:
                # Don't want any repeats
                res.append(a[it_a])
            it_a += 1
            it_b += 1
        else:
            it_b += 1
    return res
 

def merge_disjoint_intervals(a, d):
    """
    Take an array with disjoint closed intervals and a new interval and merge
    the newly covered ints into a new set of disjoint closed intervals.

    Args:
        a: A list of disjoint intervals sorted by left endpoint.
        d: A new interval

    Idea: Since the list is sorted, find the first and last interval with 
    overlap on d. If no overlap, insert d in ordered position (O(N)). If there 
    is overlap, delete all completely covered intervals and update the enpoint
    intervals. Time: O(N), Space: O(1)

    a = [(-4, -1), (0, 2), (3, 6), (7, 9), (11, 12), (14, 17)]
    d = (1, 8)
    start, end, res
    (-4, -1): 1, 8, [(-4, -1)]
    (0, 2): 0, 8, [(-4, -1)]
    (3, 6): 0, 8, [(-4, -1)]
    (7, 9): 0, 9, [(-4, -1), (0, 9)]
    (11, 12): 0, 9, [(-4, -1), (0, 9), (11, 12)]
    (14, 17): 0, 9, [(-4, -1), (0, 9), (11, 12), (14, 17)]
     
    Intervals:    |----|        |----| |-----|  |------| |----|
    No overlap:          |---| 
    Span two:                      |-----|
    Contained:                          |--|
    """

    start, end = d
    res = []
    i = 0
    while (i < len(a) and a[i][1] < start):
        res.append(a[i])
        i += 1
    while (i < len(a) and a[i][0] < end):
        # Some overlap bc a[i][1] > start and a[i][0] < end
        start = min(start, a[i][0])
        end = max(end, a[i][1])
        i += 1
    res.append((start, end))
    while (i < len(a)):
        res.append(a[i])
        i += 1
    return res


def max_interval_overlap(a):
    """
    Determine the maximum number of overlapping intervals.

    Args:
        a: A list of disjoint intervals sorted by left endpoint.

    Idea: Iterate through events and put each in a min heap keyed by endpoint.
    When the next interval starts, check to see if any of the others have ended.
    If so, pop them from the heap before counting the size of the heap. Record
    the biggest size seen.

    Time: O(NlogN) in the case that all events are overlapping
    Space: O(N)

    a = [(0, 3), (2, 3), (4, 10), (5, 8), (6, 9), (10, 11), (11, 12)]
    max_overlap, heap
    0, []
    (0, 3): 1, [3]
    (2, 3): 2, [3, 3]
    (4, 10): 2, [10]
    (5, 8): 2, [10, 8]
    (6, 9): 3, [10, 8, 9]
    (10, 11): 3 [11]
    (11, 12): 3 [12]
    """

    heap = []
    max_overlap = 0 
    for interval in a:
        while heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        max_overlap = max(max_overlap, len(heap))
    return max_overlap


def team_photo_day(a):
    """
    Two teams both have N players and want to line up for a photo shoot.
    Given a 2xN array of person heights, find an ordering for the two arrays
    such that every person in the first array is shorter than their counterpart
    in the second array, or False if it is not possible.

    Args:
        a: A 2D array, where each entry is a (Name, height) tuple
    Returns:
        Bool. Whether possible to take the picture
        List. A valid configuration for a

    a = [
        [('a', 8), ('b', 5), ('c', 6), ('d', 6), ('e', 8)],
        [('a', 3), ('b', 7), ('c', 4), ('d', 7), ('e', 5)],
    [
    Ans:
    [
        [('a', 8), ('b', 5), ('c', 6), ('d', 6), ('e', 8)],
        [('b', 7), ('a', 3), ('c', 4), ('e', 5), ('d', 7)],
    [

    Brute force: try all permutations of first array and check condition for
    each. Time: O((N+1)!), Space: O(N)

    Idea: If sorted both arrays should get close to the correct order.
    Intuitvely need the tallest person in the back to "cover" for the tallest
    in the front.
    [
        [('b', 5), ('c', 6), ('d', 6), ('a', 8), ('e', 8)],
        [('a', 3), ('c', 4), ('e', 5), ('b', 7), ('d', 7)]
    ]
    Seems to work for my baby example, but what about this counterexample:
    [
        [('b', 4), ('c', 5), ('d', 5), ('a', 8), ('e', 8)],
        [('a', 3), ('c', 4), ('e', 5), ('b', 5), ('d', 7)]
    ]
    Actually no counterexample possible. I wanted the 8 to have to 'cover' for a
    tie in the 5s but then the stray 5 would have to cover for something at
    least as big in the 8s place. So sorting seems to work.
    """

    a[0].sort(key=lambda x: x[1])
    a[1].sort(key=lambda x: x[1])

    if not all(a[0][i][1] > a[1][i][1] for i in range(len(a[0]))):
        return False, None
    return True, a
    

