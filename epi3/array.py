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


def increment_int(a):
    """Add one to base 10 int represented by array.
    
    Idea: If last entry < 9, just increment. However, if some sequence of
    trailing 9s then need to find last nine and then increment following number
    then zero out the 9s.

    Time: O(N)
    Space: O(1)

    Example 1:
    [1, 2, 3] -> [1, 2, 4] Easy!

    Example 2:
    [1, 9, 9] -> [2, 0, 0]
    Last nine is in position 1, so increment position zero. Then zero out rest.
    num_nines = 2
    a[-1] = 0
    a[-2] = 0
    a[-3] = 1

    Example 3:
    [9, 9, 9]
    Here all the 9s, so need to extend array and start from scratch.

    Note: book says to iterate once through array backward using reversed()
    """

    # Number of trailing nines
    num_nines = 0
    while num_nines < len(a):
        if a[-(num_nines + 1)] == 9:
            num_nines += 1
        else:
            break

    if num_nines == len(a):
        # Rewrite entire digit
        a[0] = 1
        for i in range(1, len(a)):
            a[i] = 0
        a.append(0)
    elif num_nines == 0:
        # Just add one to last digit
        a[-1] = a[-1] + 1
    else:
        # Carry the ones
        for i in range(num_nines):
            a[-(i + 1)] = 0
        a[-(num_nines + 1)] = a[-(num_nines + 1)] + 1


def del_dups(a):
    """Delete all the duplicates from an array..

    Idea: Maintain a pointer to the last valid digit and write the unique values
    to that pointer. Maintain a set to record all seen values.

    Time: O(N)
    Space: O(N)

    Example: 
    [5, 2, 5, 3]
    pos = 0, set = ()
    [5, 2, 5, 3]
    pos = 1, set = (5)
    [5, 2, 5, 3]
    pos = 2, set = (5, 2)
    [5, 2, 5, 3]
    pos = 2, set = (5, 2)
    [5, 2, 5, 3]
    pos = 3, set = (5, 2, 3)
    [5, 2, 3, 3]
    """

    pos = 0
    s = set()
    for i in range(len(a)):
        if a[i] not in s:
            a[pos] = a[i]
            pos += 1
            s.add(a[i])

    if pos == len(a):
        return

    for i in range(pos, len(a)):
        # Zero out remaining entries
        a[i] = 0

