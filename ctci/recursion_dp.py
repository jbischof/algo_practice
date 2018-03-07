"""Recursion and dynamic programming problems."""

def ways_to_n(n):
  """Count the number of ways to count to `n` adding the number 1, 2, or 3.
  
  Time complexity: O(N)
  Space complexity: O(N)
  """

  memo = [-1] * n 
  return ways_to_n_helper(n, memo)


def ways_to_n_helper(n, memo):
  """Recursive function to count the ways using memoization."""

  # Base cases and memoization
  if n == 0:
    return 1
  if n < 0:
    return 0
  if memo[n-1] > 0:
    return memo[n-1]
  # Compute ways to n
  memo[n-1] = (
      ways_to_n_helper(n-1, memo) +
      ways_to_n_helper(n-2, memo) + 
      ways_to_n_helper(n-3, memo))
  return memo[n-1]
  

def maze_runner(maze):
  """Find path through array-specified maze if possible.

  Time complexity: O(mn) since can only visit each cell once
  Space complexity: O(mn) for the memo
  
  Args:
    maze: A binary mXn array where ones are passable squares and zeroes are
          obstacles. Start and finish coordinates are [0, 0] and [m-1, n-1]
          respectively.
  Returns:
    An array of coordinates specifying the path.
    """

  path = []
  if not maze:
    return path
  m, n = len(maze), len(maze[0])
  memo = set() 
  maze_runner_helper(maze, m - 1, n - 1, path, memo)
  return path


def maze_runner_helper(maze, r, c, path, memo):
  """Recursive function to help find maze path.

  Args:
    maze: A binary mXn array where ones are passable squares and zeroes are
          obstacles.
    r, c: The destination
    path: The current path
    memo: Memo of unsuccessful paths
  """
    
  if not maze[r][c] or (r, c) in memo or r < 0 or c < 0:
    return False

  if (
      (r == 0 and c == 0) or  # at start 
      maze_runner_helper(maze, r - 1, c, path, memo) or  # feasible path left
      maze_runner_helper(maze, r, c - 1, path, memo)):  # feasible path up 
    path.append((r, c))
    return True

  memo.add((r, c))
  return False
