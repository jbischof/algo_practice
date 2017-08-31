"""Adventures in dynamic programming, the end boss of algo."""

def fib(n):
  """Calculate Fibonacci number using dynamic programming.
  
  Time complexity: O(n)
  Space complexity: O(1)
  """

  if n == 0:
    return 0
  if n == 1:
    return 1
  fib_im1, fib_i = 0, 1
  for j in range(2, n + 1):
    fib_im1, fib_i = fib_i, fib_im1 + fib_i
  return fib_i


def count_score_combinations(plays, score):
  """Count the number of combinations of plays that can produce a final score.

  Uses dynamic programming to build up count from lowest to highest scores.
  Time complexity: O(PS)
  Space complexity: O(PS)
  P: number of plays, S: score

  Args:
    plays: Vector of values for each possible play.
    score: Final score.
  Returns:
    Count of number of combinations.
  """
  
  plays.sort()
  # Matrix of score combinations
  # Be careful about creating separate list for each row 
  A = [([1] + [0] * score)[:] for _ in plays] 
  
  # Fill in first row of A
  A[0] = [int(s % plays[0] == 0) for s in range(score + 1)] 
  for p in range(1, len(plays)):
    value = plays[p]
    for s in range(score + 1):
      combs_without = A[p - 1][s]
      combs_with = A[p][s - value] if s >= value else 0
      A[p][s] = combs_without + combs_with      

  return A[-1][-1]


def edit_distance(a, b):
  """Compute the edit distance between strings a and b (symmetric).
  
  Time complexity: O(len(a) * len(b))
  Space complexity: O(len(a) * len(b))

  Args:
    a, b: strings
  Returns:
    Edit distance
  """

  # Matrix to hold results for recursive calls
  # A[i, j] is _edit_distance_helper(a[:i], b[:j])
  n, m = len(a), len(b)
  A = [([-1] * (m + 1))[:] for _ in range(n + 1)] 

  return _edit_distance_helper(n, m, a, b, A)


def _edit_distance_helper(i, j, a, b, A):
  """Helper function to compute edit distance.

  Args:
    i, j: Index (1-based) to truncate a, b (only working on prefixes)
    a, b: Strings with which to compute edit distance
    A: Array to store intermediate results (or -1 if not yet computed)
  Returns:
    Edit distance between a[:i] and b[:j]
  """

  # If this calculation already done, return that
  if A[i][j] >= 0:
    return A[i][j]

  # If one of indicies is zero, need to edit away rest of other 
  if not i or not j:
    A[i][j] = i if i else j 
    return A[i][j]

  # If endings are identical, no edit needed
  if a[i - 1] == b[j - 1]:
    A[i][j] = _edit_distance_helper(i - 1, j - 1, a, b, A)
    return A[i][j]
  
  # Otherwise need to deal with three edit types
  del_ed = _edit_distance_helper(i - 1, j, a, b, A)
  sub_ed = _edit_distance_helper(i - 1, j - 1, a, b, A)
  ins_ed = _edit_distance_helper(i, j - 1, a, b, A)
  A[i][j] = 1 + min([del_ed, sub_ed, ins_ed])
  return A[i][j]
