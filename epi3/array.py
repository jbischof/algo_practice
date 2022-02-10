"""Array problems."""

def sort_even_odd(a):
    """Sort array such that even entries proceed odd ones.

    Strategy: maintain pointers to even, unsorted, and odd partitions and swap
    entries in place while iterating through array.

    Time complexity: O(N), Space complexity: O(1)

    Args:
        a: array
    Returns:
        Null

    Example array:
    [1, 7, 3, 9, 4, 5]
    first_unk, last_unk = 0, 5
    -> 1 is odd, so swap with 5 and decrement last_unk
    [5, 7, 3, 9, 4, 1]
    first_unk, last_unk = 0, 4
    -> 5 is odd so swap with 4 and last_unk--
    [4, 7, 3, 9, 5, 1]
    first_unk, last_unk = 0, 3
    -> 4 is even so first_unk++
    [4, 7, 3, 9, 5, 1]
    first_unk, last_unk = 1, 3
    -> 7 is odd so swap with 9 and last_unk--
    [4, 9, 3, 7, 5, 1]
    first_unk, last_unk = 1, 2
    -> 9 is odd so swap with 3 and last_unk--
    [4, 3, 9, 7, 5, 1]
    first_unk, last_unk = 1, 1
    -> break_loop
    """

    first_unk, last_unk = 0, len(a) - 1
    while first_unk < last_unk:
        if a[first_unk] % 2 == 0:
            first_unk += 1
        else:
            a[first_unk], a[last_unk - 1] = a[last_unk - 1], a[first_unk]
            last_unk -= 1

