"""Dynamic programming problems."""

def max_subarray(a):
  """Return indices of subarray with max sum.

  Time complexity: O(n)
  Space complexity: O(1)
  """

  cum, min_cum, best_sum, min_index = 0, 0, 0, -1
  best_index = (0, 0)

  for i in range(len(a)):
    cum += a[i]
    if cum - min_cum >= best_sum:
      best_index = (min_index + 1, i)
      best_sum = cum - min_cum

    if cum <= min_cum:
      min_cum = cum
      min_index = i
    
  return best_index


def score_combs(score, plays):
  """Determine how many ways to produce score from plays.

  Time complexity: O(score * len(plays))
  Space complexity: O(score * len(plays))

  Args:
    score: int
    plays: sorted array of ints
  
  Returns:
    Int
  """

  combs = [[1] + [0] * score for play in plays]

  for k in range(len(plays)):
    for j in range(1, score + 1):
      if k > 0:
        combs[k][j] += combs[k - 1][j]
      if j >= plays[k]:
        combs[k][j] += combs[k][j - plays[k]]

  return combs[len(plays) - 1][score]


def highest_value_path(sea):
  """Finds the value of the best path through the sea.

  All paths start at upper right and end at lower left. Only moves down and to
  the right allowed.

  Time complexity: O(n^2), where n size of square
  Space complexity: O(n^2)

  Args:
    sea: A square 2x2 array with values for entries

  Returns:
    Total value of best path.
  """

  memo = [[None] * len(sea) for _ in range(len(sea))]

  return highest_value_helper(0, 0, sea, memo)


def highest_value_helper(i, j, sea, memo):
  if i >= len(sea) or j >= len(sea):
    # Base case: over the edge
    return 0

  if memo[i][j] is not None:
    return memo[i][j]

  memo[i][j] = sea[i][j] + max(
      highest_value_helper(i + 1, j, sea, memo),
      highest_value_helper(i, j + 1, sea, memo))

  return memo[i][j]


def choose(n, k):
  """Compute binomial coefficients using recursion.

  Time complexity: O(n*k)
  Space complexity: O(n*k)
  """

  memo = [[None] * k for _ in range(n)]

  return choose_helper(n, k, memo)


def choose_helper(n, k, memo):
  if n == k or k == 0:
    # Base cases: choose everything or choose nothing
    return 1

  if memo[n - 1][k - 1]:
    return memo[n - 1][k - 1]

  memo[n - 1][k - 1] = (
      choose_helper(n - 1, k, memo) + choose_helper(n - 1, k - 1, memo))

  return memo[n - 1][k - 1]
  

def choose_float(n, k):
  """Simpler version of choose function using floats to prevent overflow."""

  prod = 1
  for i in range(1, n - k + 1):
    prod *= (k + i) / float(i)

  return prod
