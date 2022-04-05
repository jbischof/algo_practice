"""Hash problems."""
from collections import Counter

def is_perm_palindrome(s):
    """
    Check whether string s can be permuted to form a palindrome.

    E.g., "edified" -> "deified"
    
    Idea: Order of the original word unimportant. All we need for a palindrome
    is that all the letters are in pairs (if even count) or all except one.
    Therefore put the individual chars as keys in a counter and then check if
    all (or all but one) pairs.
    Time: O(N), Space: O(N)
    """
    
    count = Counter()
    for char in s:
        count[char] += 1
    odd_counts = 0
    for char in count:
        if count[char] % 2 > 0:
            odd_counts += 1
    if odd_counts > 1:
        return False
    return True


def top_student(records):
    """
    Scans a CSV of student records to find the student with the top average
    test score in the highest scoring 2-3 tests.

    Args:
        records: A list of parsed file lines with a student id and test score
                 between 0 and 100. For example, "1234,98"
    Returns:
        Int. Student id with the highest average score over at least three 
        tests.

    Brute force: Create a map keyed on student id and store a heap as value with
    the top 3 test scores. Then iterate through keys and compute the average 
    score for each student, keeping track of the max score and student id seen 
    so far and return that.
    Time: O(N), Space: O(M), where N is the number of scores and M is the number
    of unique students. 

    Actually it's hard to imagine doing much better because have to read through
    all the scores and accumulate averages. Therefore the time and space are
    closely tied to N and M.

    This one is a bit too easy to bother coding up. We pass.
    """
    
    pass


def smallest_subarray_with_words(text, words):
    """
    Find the smallest contiguous subarray in a text contains all the words in a
    set.

    Args:
        text: An array of words
        words: A set of words to look for.

    Brute force: Examine every subarray, storing the smallest so far containing
    all the words. 
    Time: O(N^2K), Space: O(K), where N is the length of the text and K is the
    number of words in the set (which all must be checked using an intermediate
    set). Note that I'm not including the return value in the space cost.

    Idea: Use two pointers to traverse array. Advance the upper pointer until
    all the words are covered, then advance the lower pointer until hit another 
    one of the words. Record the smallest subarray seen so far while traversing.
    Time: O(N), Space: O(K)
    => This one seems hard to beat.

    Example text:
     0         1      2       3      4        5     6         7       8
    ["should", "not", "save", "the", "union", "or", "should", "save", "the", 
    9
    "best"]
    words = set("save", "the", "union")
    lower, upper, best_lower, best_upper, curr_words
    0, 0, -Inf, 0, []
    0, 2, -Inf, 0, ["save": 1]
    0, 3, -Inf, 0, ["save": 1, "the": 1]
    0, 4, -Inf, 0, ["save": 1, "the": 1, "union": 1]
    2, 4, 2, 4, ["save": 1, "the": 1, "union": 1]
    3, 4, 2, 4, ["the": 1, "union": 1]
    3, 7, 2, 4, ["the": 1, "union": 1, "save": 1] => not optimal
    4, 7, 2, 4, ["union": 1, "save": 1]
    4, 8, 2, 4, ["union": 1, "save": 1, "the": 1] => not optimal
    5, 8, 2, 4, ["save": 1, "the": 1]
    5, 9, 2, 4, ["save": 1, "the": 1]
    break
    return (2, 4)
    """

    lower, upper = 0, 0
    curr_words = Counter()
    best_lower, best_upper= -float("inf"), 0
    remaining_words = len(words)
    while lower <= upper and upper < len(text) - 1:
        if remaining_words > 0:
            upper += 1
            if text[upper] in words:
                curr_words[text[upper]] += 1
                if curr_words[text[upper]] == 1:
                    remaining_words -= 1
        else:
            # Valid subarray
            # Advance lower pointer until hit a word
            # Makes sure array isn't suboptimally long
            while text[lower] not in words:
                lower += 1 
            if best_upper - best_lower > upper - lower:
                best_upper, best_lower = upper, lower
            # Get rid of lowest word
            curr_words[text[lower]] -= 1
            if curr_words[text[lower]] == 0:
                remaining_words += 1
            lower += 1

    return best_lower, best_upper


def longest_unique_subarray(a):
    """
    Finds the length of the longest subarray in a that contains unique items.

    Brute force: enumerate all the subarrays and verify whether each one has
    unique entries using a hashmap. Time: O(N^3), Space: O(N)

    Idea: Move a start and end pointer through the array focusing on windows
    with unique entries. If everything is unique, advance the right pointer.
    If there is a duplicate, advance the left pointer until again all unique.
    Time: O(N) since the pointers advance N times each and each item is added
    and removed from the hashmap N times.
    Space: O(N) for the hashmap

    Book tip: store the most recent position of each item in the set so can
    advance the left pointer directly rather than position by position. Doesn't
    affect worse case but would help best and average.

              0  1  2  3  4  5  6  7  8  9
    Example: [f, s, f, e, t, w, e, n, w, e]
    s, e, ml, set
    0  0  1   [f]
    0, 1, 2,  [f, s]
    1, 1, 2,  [s]
    1, 2, 2,  [s, f]
    1, 3, 3,  [s, f, e]
    1, 4, 4,  [s, f, e, t]
    1, 5, 5,  [s, f, e, t, w]
    2, 5, 5,  [f, e, t, w]
    3, 5, 5,  [e, t, w]
    4, 5, 5,  [t, w]
    4, 6, 5,  [t, w, e]
    4, 7, 5,  [t, w, e, n]
    5, 7, 5,  [w, e, n]
    6, 7, 5,  [e, n]
    6, 8, 5,  [e, n, w]
    7, 8, 5,  [n, w]
    7, 9, 5,  [n, w, e]
    return 5
    """

    items = set([a[0]])
    start, end = 0, 0
    max_len = 1
    while end < len(a) - 1 and start <= end:
        # Check if next item can be added to set
        if a[end + 1] in items:
            # Already have that item! Remove the earliest and try again
            items.remove(a[start])
            start += 1
        else:
            # Unique item to add!
            end += 1
            items.add(a[end])
            max_len = max(len(items), max_len)
    return max_len


def longest_consecutive_subarray(a):
    """
    Find the longest subarray where all integers are consecutive. The subarray
    does not need to be contiguous in the original array.

    Brute force: Sort the array. Then traverse with a counter and reset the 
    counter every time you find a missing integer.
    Time: O(NlogN), Space: O(1)

    Idea: Iterate the array with a hashmap storing the start and end values of
    clusters of consecutive ints. Then as go through the array need to check
    if value belongs to any of the existing clusters. If not, form a new one.
    Issue: how do you key an entry by both the start and the end? Also hard to 
    know how to merge these clusters.

    Idea2: Use a set and seed it with all the items in the array. Then while
    traversing the set can search for neighboring values and pop them to form a 
    cluster.
    Time: O(N), Space: O(N)

    Example:
    a = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
    ans: 6 from [-2, -1, 0, 1, 2, 3]

    nums = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5]
    val, cc, mc, nums (after)
    3,   6,  6,  [5]
    7,   3,  6
    5,   1,  6
    """

    nums = set(a)
    max_clust = 0

    while nums:
        val = nums.pop()
        curr_clust = 1
        # Search below
        j = val - 1
        while j in nums:
            curr_clust += 1
            nums.discard(j)
            j -= 1
        # Search above
        k = val + 1
        while k in nums:
            curr_clust += 1
            nums.discard(k)
            k += 1
        if curr_clust > max_clust:
            max_clust = curr_clust
        nums.discard(val)

    return max_clust


