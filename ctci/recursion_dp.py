"""Recursion and dynamic programming problems."""
import copy
import collections

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
  _maze_runner_helper(maze, m - 1, n - 1, path, memo)
  return path


def _maze_runner_helper(maze, r, c, path, memo):
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
      _maze_runner_helper(maze, r - 1, c, path, memo) or  # feasible path left
      _maze_runner_helper(maze, r, c - 1, path, memo)):  # feasible path up 
    path.append((r, c))
    return True

  memo.add((r, c))
  return False


def magic_index(a):
  """Find index in sorted, unique, integer array with a[i] = i.

  Returns `None` if no such index exists.
  
  Time complexity: O(logN)
  Space complexity: O(1)
  """

  start, end = 0, len(a) - 1
  while start <= end:
    mid = (start + end) // 2
    if a[mid] == mid:
      return mid
    if a[mid] > mid:
      end = mid - 1
    elif a[mid] < mid:
      start = mid + 1
  return None
  

def power_set(a):
  """Return the power set of a set.

  Args:
    a: A set
  Returns:
    List of all sets in power set
  """

  # Base case: empty set
  if not a:
    return [set()]
  # Recursion: P(a) = P(a \ x) U x + P(a \ x)
  item = next(iter(a))
  a_less_item = copy.deepcopy(a)
  a_less_item.remove(item)
  pset_less_item = power_set(a_less_item)
  pset_with_item = copy.deepcopy(pset_less_item)
  for value in pset_with_item:
    value.add(item)
  return pset_less_item + pset_with_item


def permutations(s):
  """Returns set of all permutations of string s.
  
  Time complexity: O(N^2 * N!) because N! permutations and string manipulation
                   costs O(N) per recursive call and N calls to get string.
  Space complexity: O((N-1)!) for stack of recursive calls.
  """

  ret = set()
  _permutations_helper('', s, ret)
  return ret


def _permutations_helper(prefix, remain, ret):
  """Recursive function to compute all perms conditional on prefix."""

  # Base case: all chars in `prefix`
  if not remain:
    ret.add(prefix)
  # Otherwise iterate through chars in `remain` and add to `prefix`.
  for i in xrange(len(remain)):
    _permutations_helper(prefix + remain[i], remain[:i] + remain[i+1:], ret)


def permutations_no_dups(s):
  """Returns set of all permutations of string with no duplicates.

  If no duplicate chars in `s` algorithm the same as before but if there are
  then need to only iterate through unique chars in loop.
  
  Time complexity: O(N^2 * N!) because N! permutations and string manipulation
                   costs O(N) per recursive call and N calls to get string.
  Space complexity: O(N) for stack of recursive calls.
  """

  # Need `ret` as list or won't be able to tell if dups eliminated.
  ret = []
  _permutations_no_dups_helper('', collections.Counter(s), ret)
  return ret


def _permutations_no_dups_helper(prefix, remain, ret):
  """Recursive function to compute all perms conditional on prefix.
  
  Args:
    prefix: String with chars already in perm.
    remain: collections.Counter of remainings chars
    ret: List of completed permutations.
  """

  # Remove empty keys in counter
  remain += collections.Counter()
  # Base case: all chars in `prefix`
  if not remain:
    ret.append(prefix)
  # Otherwise iterate through unique chars in `remain` and add to `prefix`.
  for char in remain:
    if remain[char]:
      remain.subtract(char)
      _permutations_no_dups_helper(prefix + char, copy.deepcopy(remain), ret)
      remain.update(char)


def all_parens(n):
  """Return list of all possible strings with `n` valid pairs of parens."""

  ret = []
  _all_parens_helper(bytearray(''), 0, n, ret)
  return ret


def _all_parens_helper(prefix, opened, remaining, ret):
  """Recursive function to create list of possible pairs of parens.

  Args:
    prefix: String so far
    opened: Number of parens opened
    remaining: Number of parens left to be opened
    ret: List of completed strings
  """
  # If nothing left to open and nothing remaining, string complete
  if not opened and not remaining:
    ret.append(str(prefix))

  # Close a paren if one left
  if opened:
    prefix.append(')')
    _all_parens_helper(copy.deepcopy(prefix), opened - 1, remaining, ret)
    prefix.pop()
  # Open a paren if one left
  if remaining:
    prefix.append('(')
    _all_parens_helper(copy.deepcopy(prefix), opened + 1, remaining - 1, ret)


def ways_to_make_change(n):
  """Count the number of ways to make change for `n` cents.

  Problem assumes standard U.S. coinage.

  Time complexity: O(N)
  Space complexity: O(N)

  Args:
    n: Number of cents needed
  Returns:
    Integer giving count of ways.
  """

  coins = (25, 10, 5, 1)
  memo = [[None] * (n + 1) for j in xrange(len(coins))]
  return _ways_to_make_change_helper(n, coins, 0, memo)


def _ways_to_make_change_helper(n, coins, index, memo):
  """Recursive function to compute ways to make change for `n` cents.

  Args:
    n: Number of cents needed
    coins: List of coin denominations (in decreasing order)
    index: Index of coin currently in consideration
    memo: Memo of previous (up to index, n) combinations computed
  Returns:
    Integer giving count of ways.
  """

  # Base case: tally reaches `n`
  if n == 0:
    return 1

  # Otherwise out of denominations, so give up
  if index >= len(coins):
    return 0

  # Look up memoized answer if available
  if memo[index][n] is not None:
    return memo[index][n]

  val = coins[index]
  ans = 0
  j = 0  # Number of coins of this type used
  while j * val <= n:
    ans += _ways_to_make_change_helper(n - j * val, coins, index + 1, memo) 
    j += 1

  memo[index][n] = ans
  return ans


def ways_to_make_change_iter(n):
  """Iterative version of `ways_to_make_change`.

  Same time and space complexity, but avoiding recursion.

  Key insight: iterate through memo explicitly using recursion
    num_ways(n, coins[1, ..., k]) = 
        num_ways(n, coins[1, ..., k - 1]) +
            num_ways(n - j*val, coins[1, ..., k])
  First row needs to be filled in manually. First column (n=0) will be set to 1.

  Args:
    n: Number of cents needed
  Returns:
    Integer giving count of ways.
  """

  coins = (1, 5, 10, 25)
  memo = [[None] * (n + 1) for j in xrange(len(coins))]
  memo[0] = [int(j % coins[0] == 0) for j in xrange(n + 1)]
  for k in xrange(1, len(coins)):
    val = coins[k]
    memo[k][0] = 1
    for j in xrange(1, n + 1):
      ways_without_k = memo[k - 1][j]
      ways_with_k = memo[k][j - val] if j - val >= 0 else 0
      memo[k][j] = ways_without_k + ways_with_k
  return memo[len(coins) - 1][n]


class Box(object):
  def __init__(self, width, length, height):
    self.width = width
    self.length = length
    self.height = height
    self.best_height = None 

  def __lt__(self, other):
    return (
        self.width < other.width and 
        self.height < other.height and 
        self.length < other.length)

  def __gt__(self, other):
    return (
        self.width > other.width and 
        self.height > other.height and 
        self.length > other.length)


def highest_box_stack(boxes):
  """Determine highest possible stack of boxes.

  Only boxes with strictly larger width, height, and length can be placed
  underneath another. Uses graph representation where directed edge A->B means
  that vertex `A` can be stacked below vertex `B`.

  Time complexity: O(|V|^2 + |E|), where |V| is the number of boxes and |E| is
      number of pairs that are stackable (can absorb into |V|^2 for worst case).
      While each node and edge only visited once, takes |V|^2 time to construct
      the graph.
  Space complexity: O(|V| + |E|) for recursion stack, graph and memo. If just 
      taking edges as worst case, O(|V|^2)

  Args:
    boxes: An iterable of `Box` objects.
  Returns:
    Float with highest value.
  """

  # Make graph out of boxes so only do size comparisons once.
  # Directed edge A->B means that box `A` can be placed under box `B`.
  graph = {}
  for j in xrange(len(boxes)):
    graph[j] = [] 
    for k in xrange(len(boxes)):
      if boxes[j] > boxes[k]:
        graph[j].append(k)

  max_height = 0
  for j in xrange(len(boxes)):
    max_height = max(
        max_height, 
        _highest_box_stack_from_index(j, graph, boxes))
  return max_height
  

def _highest_box_stack_from_index(index, graph, boxes):
  """Determine largest height of possible stack with index as lowest box."""

  # Return memo if partial stack already measured
  if boxes[index].best_height:
    return boxes[index].best_height 

  max_height = boxes[index].height

  for edge in graph[index]:
    max_height = max(
        max_height,
        boxes[index].height + _highest_box_stack_from_index(edge, graph, boxes))

  # Make memo of answer
  boxes[index].best_height = max_height
  return max_height
