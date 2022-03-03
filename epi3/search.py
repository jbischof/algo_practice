"""Search problems."""

def binary_search(t, a):
    """
    Return index of value t in array a if present. If not, returns None.

    Time: O(log N), Space: O(1)
    """

    lower, upper = 0, len(a) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if a[middle] < t:
            lower = middle + 1
        elif a[middle] == t:
            return middle
        else:
            upper = middle - 1

    return None


def binary_search_first(t, a):
    """
    Find the **first** occurrence of value t in array a if present. If not,
    returns None.

    Time: O(N), Space: O(1)
    Time linear because may have to backtrack through half of the array if
    entire array is value t.
    """

    lower, upper = 0, len(a) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if a[middle] < t:
            lower = middle + 1
        elif a[middle] == t:
            # Backtrack if previous value also satisfies query
            while middle > 0 and a[middle - 1] == t:
               middle -= 1 
            return middle
        else:
            upper = middle - 1
    return None


def binary_search_first2(t, a, debug = False):
    """
    Find the **first** occurrence of value t in array a if present. If not,
    returns None.

    Improving on previous version to recover log N time complexity.

    Time: O(log N), Space: O(1)

    Example:
         0, 1, 2, 3, 4, 5, 6, 7, 8
    a = [1, 2, 3, 3, 3, 3, 3, 5, 6]
    t = 3
    lower, upper, middle, a[middle]
    0, 8, 4, 3 -> upper = 3
    0, 3, 1, 2 -> lower = 1
    1, 3, 2, 3 -> return 2
    """

    lower, upper = 0, len(a) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if debug:
            print(lower, middle, upper)
        if a[middle] < t:
            lower = middle + 1
        elif (
                (a[middle] == t and middle == 0) or 
                (a[middle] == t and not a[middle - 1] == t)
            ):
            return middle
        else:
            upper = middle - 1
    return None


def kth_smallest(k, a):
    """
    Find kth smallest element of array.

    Brute force: sort the array and take the k-1 element.
    Time: O(n log k), Space: O(1)

    Idea: Randomize the array and use a pivoting strategy to divide the array
    into bigger and smaller regions.

    Take last element of region of consideration as pivot and move into final
    sorted location. Then if position < k 
     0, 1, 2, 3, 4
    [5, 2, 1, 3, 4]
    k = 3 (pos 2)
    lower, upper, i, pivot, pivot_num
    0, 4, 0, 4, 4
    => 5 > 4, swap 5 and 3 then swap 4 and 5
     0, 1, 2, 3, 4
    [3, 2, 1, 4, 5]
    lower, upper, i, pivot, pivot_num
    0, 4, 0, 3, 4
    0, 4, 1, 3, 4 => 3 < 4 so i+1
    0, 4, 2, 3, 4 => 1 > 4 so i+1, done
    => pivot now at pos 3 > 2, recurse left 
     0, 1, 2, 3, 4
    [3, 2, 1, 4, 5]
    lower, upper, i, pivot, pivot_num
    0, 2, 0, 2, 1
    => 3 > 1, swap 2 and 3 and 2 and then swap 1 and 3, pivot = 1
     0, 1, 2, 3, 4
    [2, 1, 3, 4, 5]
    lower, upper, i, pivot, pivot_num
    0, 2, 0, 1, 1
    => 2 > 1, so swap 2 and 2 and then swap 1 and 2
     0, 1, 2, 3, 4
    [1, 2, 3, 4, 5]
    lower, upper, i, pivot, pivot_num
    0, 2, 0, 0, 1
    => pivot now at pos 0 < 2, recurse right
    lower, upper, pivot_num
    1, 2, 3
     0, 1, 2, 3, 4
    [1, 2, 3, 4, 5]
    => 3 > 1, continue
    => 3 > 2, continue
    => pivot now at pos 2, return!
    """

    assert(k <= len(a))
    k_pos = k - 1
    lower, upper = 0, len(a) - 1
    while lower <= upper:
        i, pivot = lower, upper
        while i < pivot: 
            if a[i] > a[pivot]:
                a[i], a[pivot - 1] = a[pivot - 1], a[i]
                a[pivot - 1], a[pivot] = a[pivot], a[pivot - 1]
                pivot -= 1
            else:
                i += 1
        if pivot > k_pos:
            # Recurse left
            upper = pivot - 1
        elif pivot == k_pos:
            return a[pivot]
        else:
            # Recurse right
            lower = pivot + 1
    # This should never happen
    return None


def search_2d_array(a, k):
    """
    Returns true of the item k is in the 2D sorted array `a`.
    A 2D sorted array has both the rows and columns in increasing order.

    Brute force: iterate through entire array.
    Time: O(NM), Space: O(1)

    Idea: Search each row, stopping when hit the end or find a larger number.
    Then proceed to the next row (same column) and decide direction as needed.
    Unclear about the time complexity---maybe a lot of backtracking necessary?

    Idea2: Perform binary search on each row. Time(NlogM), Space: O(1)
    Even better: search the big dimension and iterate over the small.

    Idea3: Maintain a min_row, max_col of the current search area. Each
    iteration compare the top right element to the search value. If the value
    if less, increment min_row. If the value is greater, decrement max_col.
    Stop when matrix is 1x1.
    Top: O(N + M) since reduce the search area by one row or column each iter.
    Space: O(1)

    a = [#0   1   2   3    4
        [-1,  2,  4,  5,   6],   # 0 
        [ 1,  5,  5,  9,   21],  # 1
        [ 3,  6,  6,  9,   22],  # 2
        [ 3,  6,  8,  10,  24],  # 3
        [ 6,  8,  9,  12,  25],  # 4 
        [ 8,  10, 12, 13,  40],  # 5
    ]
    7 -> False
    min_row, max_col, num
    0, 4, 6 < 7
    1, 4, 21 > 7
    1, 3, 9 > 7
    1, 2, 5 < 7
    2, 2, 6 < 7
    3, 2, 8 > 7
    3, 1  6 < 7
    4, 1, 8 > 7
    4, 0, 6 < 7
    5, 0, 8 > 7
    5, -1 break
    Return False
    8 -> True
    """

    min_row, max_col = 0, len(a[0]) - 1
    while min_row < len(a) and max_col > -1:
        # Check the top left corner
        if a[min_row][max_col] == k:
            return True
        if a[min_row][max_col] < k:
            max_col -= 1
        else:
            min_row += 1

        return False

