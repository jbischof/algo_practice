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
    Number of combinations.
  """
  
  plays.sort()
  # Matrix of score combinations
  A = [[1] + [0] * score for _ in plays] 
  
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

  # Matrix to hold results for unique recursive calls
  # A[i, j] is _edit_distance_helper(a[:i], b[:j])
  n, m = len(a), len(b)
  A = [[-1] * (m + 1) for _ in range(n + 1)] 

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


def count_array_traversals(n, m):
  """Count number of paths to traverse n x m 2D array.

  Start at upper right; only possible moves are right and down.
  Note: Analytic solution is choose(n + m - 2, m - 1)
  Time complexity: O(n * m)
  Space complexity: O(n * m)

  Args:
    n, m: dimensions of array
  Returns:
    Count of paths
  """

  # Matrix to hold results for recursive calls
  A = [[-1] * m for _ in range(n)] 

  # Record base case
  A[0][0] = 1

  # Start at end and work way back to beginning
  return _count_array_traversals_helper(n - 1, m - 1, A)


def _count_array_traversals_helper(i, j, A):
  # If this calculation already done, return that
  # Includes base case of (0, 0)
  if A[i][j] >= 0:
    return A[i][j]

  # Answer is sum of up and left paths unless already at edge
  ans = 0
  if i > 0:
    ans += _count_array_traversals_helper(i - 1, j, A)
  if j > 0:
    ans += _count_array_traversals_helper(i, j - 1, A)
  A[i][j] = ans
  return ans


class Item(object):
  """Class to hold item metadata for knapsack problem."""
  def __init__(self, label, weight, value):
    self.label = label 
    self.weight = weight
    self.value = value


def knapsack(items, max_weight):
  """Find combination of items with max value given weight constraint.

  Time complexity: O(n * max_weight)
  Space complexity: O(n * max_weight)

  Args:
    items: list of Item objects
    max_weight: maximum weight capacity of knapsack
  Returns:
    Value of best combination
  """

  n = len(items)
  # N x (max_weight + 1) matrix of memoized best values
  # Need first column to be zero weight so that can consider replacing entire
  # contents of knapsack
  A = [[0] * (max_weight + 1) for _ in range(n)]
  # Fill in first row
  for w in range(max_weight + 1):
    A[0][w] = items[0].value if items[0].weight <= w else 0
  for i in range(1, n):
    for w in range(max_weight + 1):
      weight, value = items[i].weight, items[i].value
      # Can't add item if already too heavy for weight
      best_value_with = A[i - 1][w - weight] + value if weight <= w else 0
      best_value_without = A[i - 1][w]
      A[i][w] = max(best_value_with, best_value_without) 
  return A[-1][-1]
