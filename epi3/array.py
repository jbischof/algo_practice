"""Array problems."""
import random

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


def len_longest_equal_subarray(a):
    """Finds the length of the longest subarray where all entries are equal.

    Idea: Record the previous value and a counter for how long since that 
    value has been the same. Once the value changes, compare that counter to
    the longest subarray seen so far.

    Time: O(N) since only traverse array once, Space: O(1)

    a = [3, 3, 4, 5, 5, 5, 6]
    3: 0, 1, 3
    3: 0, 2, 3
    4: 2, 1, 4
    5: 2, 1, 5
    5: 2, 2, 5
    5: 2, 3, 5
    6: 3, 1, 6
    Return: 3
    """

    len_longest = 0
    len_so_far = 1
    last_seen = a[0]
    
    for x in a[1:]:
        if x == last_seen:
            len_so_far += 1
        else:
            if len_so_far > len_longest:
                len_longest = len_so_far
            len_so_far = 1
            last_seen = x

    return len_longest


def rand_permutation(a):
    """Compute a random permutation of array.

    Strategy: Iterate through array and fill each position with an item
    remaining from the rest of the list.

    Time: O(N), Space: O(1)

    """

    for i in range(len(a)):
        j = random.randrange(i, len(a))
        a[i], a[j] = a[j], a[i]


def subarray_sum(a, k):
    """Check if any subarray sums to integer k.

    Args:
        a: array on ints
    Returns:
        bool if subarray exists

    Idea: Iterate through the array and record all cumulative sums sum(a[:k])
    in a hashmap. While iterating check if (k - sum) is the the table.
    """

    sums = set()
    cum_sum = 0

    for x in a:
        sums.add(cum_sum)
        cum_sum += x
        if cum_sum - k in sums:
            return True
    return False


def best_trade(a):
    """
    Find the best times to buy and sell a stock
    Args:
        a: array of prices time series
    Returns:
        A tuple of buy and sell times
        
    Idea: Iterate through the array and keep a running min since that is always
    the best time to buy. Then compare the current price to the running min and
    see if current profit better than the highest seen so far.
    Time: O(N), Space: O(1)

         0  1  2  3  4  5  6
    a = [5, 3, 7, 8, 2, 1, 4]
    idx, bt, bt_idx,  run_min, argmin
    0,   -2, (0, 1),  5,       0      
    1,   -2, (0, 1),  3,       1      
    2,   4,  (1, 2),  3,       1      
    3,   5,  (1, 3),  3,       1      
    4,   5,  (1, 3),  2,       4      
    5,   5,  (1, 3),  1,       5
    6,   5,  (1, 3),  1,       5
    return (1, 3)
    """

    # Initialize with first price
    run_min = a[0]
    argmin = 0
    best_trade_idx = (0, 1)
    best_trade = a[1] - a[0]
    for i in range(1, len(a)):
        price = a[i]
        if price - run_min > best_trade:
            best_trade_idx, best_trade = (argmin, i), price - run_min
        if price < run_min:
            argmin, run_min = i, price
    return best_trade_idx
