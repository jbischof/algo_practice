"""Dynamic programming problems."""

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
    memo = [1] * len(a - 1)

    for i in range(1, len(a)):
        ans = 1
        for j in range(i):
            if a[j] <= a[i]:
                ans = max(ans, memo[j] + 1)
        memo[i] = ans
    return max(memo)

