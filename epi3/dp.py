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
