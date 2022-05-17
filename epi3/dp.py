"""Dynamic programming problems."""

def fib_bu(n):
    """
    Compute the nth fib number from the bottom up.

    Args:
        n: Int
    Returns:
        Int. Fib(n)

    f(0) = 0, f(1) = 1
    f(n) = f(n-1) + f(n-2)

    Time: O(n), Space: O(n)
    """

    # Break off initial values
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = [0] + [1] * n
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


def num_score_combs(n, scores):
    """
    Determine the number of unqiue combinations of the score values that sum
    up to n.

    Args:
        n: Total score
        scores: List of values that can be used.

    Brute force: Enumerate all the possible combinations in a giant nested loop.
    Record all those that sum up to n without going over.
    E.g., if n=8 and scores=(2, 3), then try all combinations of 2s from
    0, ..., 8 // 2 = 4 and 3s from 0, ..., 8 // 3 = 2
    Time: O(n^scores), Space: O(1)

    Idea: Compute recursively. 
    ways(n) = ways(n-scores[0]) + ways(n-scores[1]), + ... 
    For n=8 and scores=(2,3), answer is
    ways(8) = ways(6) + ways(5)
    ways(6) = ways(4) + ways(3)
    ways(5) = ways(2) + ways(3)
    ways(4) = ways(2) + ways(1)
    ways(3) = ways(1) + ways(0)
    ways(2) = ways(0) + ways(-1)
    Base case is ways(0) = 0 and ways(x < 0) = 0
    However there is clearly a lot of repeated computations here as every call
    generates len(scores) more. Therefore the computation is still exponential 
    Time: O(scores^n) and Space: O(n)

    Caching can help reduce this complexity by storing the intermediate results.
    Therefore for each n we are guaranteed only n recurive calls to the function
    Time: O(n), Space: O(n)
    Actually this does not work because it counts the ordered sets of events,
    not the combinations.

    Final idea: Start adding the scores one by one to the analysis. In this way
    we build up the memo from the bottom increasing the target score and then
    the set of considered scores in alternation.
    Example: n = 6, scores = (2, 3, 4)
    #
    [  # 0  1  2  3  4  5  6
        [1, 0, 1, 0, 1, 0, 1], # 2
        [1, 0, 1, 1, 1, 1, 2], # 2, 3
        [1, 0, 1, 1, 2, 1, 3], # 2, 3, 4
    ]
    Time: O(N * M), where N is the final score and M is the number of unique
    scores
    Space: O(N * M)
    """

    scores.sort()
    n_score = len(scores)
    memo = [[1] + [0] * n for _ in range(n_score)]

    for i, score in enumerate(scores):
        for j in range(1, n + 1):
            # Total combs are combs without score i + combs for total - score i
            memo[i][j] = (
                    (memo[i - 1][j] if i > 0 else 0) + 
                    (memo[i][j - score] if j >= score else 0)
            )
    return memo[n_score - 1][n]


def knapsack_recurse(capacity, weights, values):
    """
    Determine the optimal combination of items to maximize value under a total
    capacity constraint.

    Time: O(N*C), Space(N^2*C) to store the intermediate arrays

    Args:
        capacity: Int, total capacity of knapsack
        weights: List of weights for each item
        values: List of values for each item

    Example:
               0  1  2  3
    weights = [2, 3, 1, 4]
    values =  [4, 5, 3, 7]
    capacity = 5
    o, c, v,  items
    4, 5, 0,  []
    3, 1, 7,  [3]
    3, 5, 0,  []
    2, 0, 10, [2, 3] 
    2, 4, 3,  [2] 
    2, 1, 7,  [3] 
    2, 5, 0,  []
    1, 0, 10, [2, 3] 
    1, 4, 3,  [2] 
    1, 1, 8,  [1, 2] 
    1, 1, 7,  [3] 
    1, 2, 5,  [1]
    1, 5, 0,  []
    0, 0, 10, [2, 3] 
    0, 4, 3,  [2] 
    0, 2, 7,  [0, 2] 
    0, 1, 8,  [1, 2] 
    0, 1, 7,  [3] 
    0, 2, 5,  [1]
    0, 0, 9,  [0, 1]
    0, 5, 0,  []
    return 10, [2,3]
    """

    memo = {}
    return knapsack_recurse_helper(0, capacity, weights, values, memo)


def knapsack_recurse_helper(offset, capacity, weights, values, memo):
    """
    Recursive function that passes information UP the stack
    """

    # Base case 1: all items considered
    if offset >= len(weights):
        return 0, []

    # Base case 2: answer in memo
    if (offset, capacity) in memo:
        return memo[(offset, capacity)]

    # At each offset try to include and exclude the item
    max_without, items_without = knapsack_recurse_helper(
            offset + 1, capacity, weights, values, memo) 

    max_with = float('-inf')
    if capacity >= weights[offset]:
        # Backtrack if item cannot fit in current configration
        max_with, items_with = knapsack_recurse_helper(
                offset + 1, capacity - weights[offset], weights, values, memo) 
        max_with += values[offset]
        # Need to make copy of array every time you change it for memo to work
        items_with = items_with + [offset]

    if max_with > max_without:
        ans = max_with, items_with
    else:
        ans = max_without, items_without
    memo[(offset, capacity)] = ans
    return ans


def min_weight_path_triangle(t):
    """
    Find minimum weight path from top to bottom in a triangle.

    A path starts at the top and must descend continuously until it reaches the
    bottom row.

    Args:
        t: A nested array where len(t[i]) == i
    Returns:
        Int. The weight of the min path.

    Q: How do you determine adjacent nodes in the triangle?
    A: If at entry j of level, have access to (j, j+1) in level i+1

    Idea 1: Build solution from bottom up. At each entry [i, j], branch the
    decision to try (i+1, j) and (i+1, j+1). Base case is len(t) path, where
    you write the final sum to a ret array. For DP could memoize solutions in
    terms of i, j tuple since two ways to get to every i, j from the level i-1.
    Then total solution space is O(N^2) kinda like a lower triangular matrix.

    Idea 2: Build solution from the top down. In this case choose each entry
    in t[len(t) - 1] and then choose the min of the two paths that could have
    reached there: 
    min_path(i, j) = min(min_path(i - 1, j), min_path(i - 1, j - 1)) + t[i, j]
    In the case still want to cache the value of min_path(i, j) since will each
    entry will be called two times.
    Time: O(N^2), Space: O(N^2)

    Example:
    t = [
        #0
        [2], # level 0
        #0  1 
        [4, 4], # level 1
        #0  1  2
        [8, 5, 6], # level 2
        #0  1  2  3
        [4, 2, 6, 2], # level 3
        #0  1  2  3  4
        [1, 5, 2, 3, 4], # level 4
    ]
    Answer: 15 ([2, 4, 5, 2, 2])
    i, j
    4, 0 = min(inf, f(3, 0)) 
    3, 0 = min(inf, f(2, 0)) 
    2, 0 = min(inf, f(1, 0)) 
    1, 0 = min(inf, f(0, 0)) = 2 + 4 
    2, 0 = min(inf, 6) + 8 = 14
    3, 0 = min(inf, 14) + 4 = 18
    4, 0 = min(inf, 18) + 1 = 19
    4, 1 = min(18, f(3, 1))
    3, 1 = min(14, f(2, 1))
    2, 1 = min(6, f(1, 1))
    1, 1 = min(2, inf) + 4 = 6
    2, 1 = min(6, 6) + 5 = 11
    etc etc
    """

    memo = [[None] * (i + 1) for i in range(len(t))]
    memo[0][0] = t[0][0]
    for j in range(len(t)): 
        min_weight_path_triangle_helper(len(t) - 1, j, t, memo)
    return min(memo[-1])


def min_weight_path_triangle_helper(i, j, t, memo):
    # Base case: already in memo 
    if memo[i][j] is not None:
        return memo[i][j]

    min_left = (
            min_weight_path_triangle_helper(i - 1, j - 1, t, memo)
            if j > 0 else float('inf')
    )
    min_right = (
            min_weight_path_triangle_helper(i - 1, j, t, memo) 
            if j < len(t[i]) - 1 else float('inf')
    )
    memo[i][j] = min(min_left, min_right) + t[i][j]
    return memo[i][j]


def longest_nd_subsequence(a):
    """
    Find the length of the longest nondecreasing subsequence in an array.

    Args:
        a: Array of ints
    Returns:
        Int: length of longest nondecreasing subsequence

    Brute force: check all possible subsequences for whether non-decreasing.
    Time: O(2^N)

    Example:
         0  1  2  3   4  5   6  7   8  9 
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    Ans: [0, 4, 10, 14] and [0, 2, 6, 9], both of length 4

    
    Recursive approach: can f(a[:j]) be expressed in terms of f(a[:i]), i<j?
    if f(a[:j-1]) = k, then f(a[:j]) =
        1 + f(a[:j-1]) if a[j] > a[:j-1]

    Time: O(N^2), Space: O(N)

    i, j, ans, memo
                0  1  2  3  4  5  6  7  8  9
    -, -, -,   [1]
    1, 0, 2,   [1, 2]
    2, 0, 2
    2, 1, -,   [1, 2, 2]
    3, 0, 2
    3, 1, 3
    3, 2, 3,   [1, 2, 2, 3]
    4, 0, 2
    4, 1, -
    4, etc     [1, 2, 2, 3, 2]
    5, 0, 2
    5, 1, 3
    5, 2, 3
    5, 3, -
    5, 4, 3    [1, 2, 2, 3, 2, 3]
    6, 0, 2
    6, 1, -
    6, 2, 3
    6, 3, -
    6, 4, 3
    6, 5, -    [1, 2, 2, 3, 2, 3]
    7, 0, 2 -> bigger than everything before so 4
    7,         [1, 2, 2, 3, 2, 3, 4]
    etc
    """

    # Tablular memo. Initialize first entry to one
    memo = [1] * len(a)

    for i in range(1, len(a)):
        ans = 1
        for j in range(i):
            if a[j] <= a[i]:
                ans = max(ans, memo[j] + 1)
        memo[i] = ans
    return max(memo)


def has_array_sequence(a, s):
    """
    Find 1D sequence `s` in 2D array moving left, right, up or down in each step

    Args:
        a: A N x M 2D array
        s: A 1D array of length J

    Time: O(N x M x J), Space: O(N x M x J)

    """

    memo = {}
    ret = False
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret = ret or has_array_sequence_helper(i, j, 0, a, s, memo)
    return ret


def has_array_sequence_helper(i, j, offset, a, s, memo):
    # Base case 1: ans in memo
    if (i, j, offset) in memo:
        return memo[(i, j, offset)]

    # Base case 2: bad coordinates
    if i < 0 or i > len(a) - 1 or j < 0 or j > len(a[0]) - 1:
        return False

    # Base case 3: offset is len(s) - 1
    if offset == len(s) - 1:
        memo[(i, j, offset)] = a[i][j] == s[offset]
        return memo[(i, j, offset)] 

    # Base case 4: offset doesn't fit here
    if a[i][j] != s[offset]:
        memo[(i, j, offset)] = False
        return memo[(i, j, offset)] 

    # Otherwise recurse on the neighbors
    memo[(i, j, offset)] = any([
        has_array_sequence_helper(i + 1, j, offset + 1, a, s, memo),
        has_array_sequence_helper(i - 1, j, offset + 1, a, s, memo),
        has_array_sequence_helper(i, j + 1, offset + 1, a, s, memo),
        has_array_sequence_helper(i, j - 1, offset + 1, a, s, memo),
    ])
    return memo[(i, j, offset)] 


def equal_subset_sum(a):
    """
    Determine if the array can be partitioned into two arrays with equal sum.

    Args:
        a: Array of ints
    Returns:
        Bool: whether array can be partitioned
        List(Set): two partitions

    Brute force: Compute sum of overall array. If not a product of 2, return
    False. Otherwise try all possible subsets and see if subset sum is equal to
    half the total.
    Time: O(N 2^N), Space: O(N)

    Recursion: Let R(offset, sum) give whether can reach target sum with `sum`
    amount remaining.
    Then R(offset, sum) = R(offset + 1, sum - a[offset]) or R(offset + 1, sum)

    Time: O(N * T), Space: O(N * T), where N is length of array and T is sum.

    Example: 
    a = [1, 1, 3, 4, 7]
    asum = 16, target = 8
    Return True {4, 3, 1}, {7, 1}
    Example:
    a = [20, 1, 1, 3, 4, 7]
    asum = 36, target = 18 
    Return False
    """

    memo = {}
    asum = sum(a)
    if asum % 2 != 0:
        return False
    return equal_subset_sum_helper(0, asum // 2, a, memo)


def equal_subset_sum_helper(offset, remaining, a, memo):
    # Base case: offset at end
    if offset >= len(a):
        if remaining == 0:
            return True
        return False

    if (offset, remaining) in memo:
        return memo[(offset, remaining)]

    # Without offset
    can_without = equal_subset_sum_helper(offset + 1, remaining, a, memo)

    # With offset
    can_with = False
    remaining_with = remaining - a[offset]
    if remaining_with >= 0:
        # Backtrack if already lower than target
        can_with = equal_subset_sum_helper(offset + 1, remaining_with, a, memo)

    if can_with or can_without:
        memo[(offset, remaining)] = True
    else:
        memo[(offset, remaining)] = False 

    return memo[(offset, remaining)] 


def tokenize(s, words):
    """
    Tokenize a string with no space delimiters into possible tokens in set.

    Time: O(N^N), Space: O(N)

    Note: DP solution very hard if want all possible decompositions. This
    version is from an Amazon interview but the EPI version only asks if any
    decomposition possible.

         0123456
    s = 'anagram'
    words = set(['an', 'a', 'na', 'gram', 'anagram'])
    o, i, interp
    0, 1, ['a']
    1, 2, ['a']
    1, 3, ['a', 'na']
    3, 4, ['a', 'na']
    3, 5, ['a', 'na']
    3, 6, ['a', 'na']
    3, 7, ['a', 'na', 'gram']
    0, 2, ['an']
    2, 3, ['an', 'a']
    ...
    """
    ret = []
    tokenize_helper(0, s, [], words, ret)
    return ret


def tokenize_helper(offset, s, interp, words, ret):
    for i in range(offset + 1, len(s) + 1):
        if s[offset : i] in words:
            interp.append(s[offset : i])
            if i == len(s):
                ret.append(" ".join(interp))
            else:
                tokenize_helper(i, s, interp, words, ret)
            interp.pop()

