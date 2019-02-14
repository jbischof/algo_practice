"""Recursion problems."""
import copy

def gcd(y, x):
  """Computes the gcd of y and x where y >= x."""

  return y if x == 0 else gcd(x, y % x)


def gcd_nr(y, x):
  """Computes the gcd of y and x where y >= x without recursion.
  
  gcd() function above clearly a tail recursion, so iteration straightforward.
  """

  while x > 0:
    y, x = x, y % x
  return y

def towers_of_hanoi(n):
  """Play towers of hanoi game.

  Time complexity: O(2^n)
  Space complexity: O(1)
  
  Args:
    n: Number of discs
  
  Returns:
    Completed board.
  """

  board = [range(n - 1, -1, -1), [], []]
  hanoi_move(n, 0, 1, 2, board)
  return board


def _is_reverse_sorted(a):
  """Check if array is reverse sorted."""

  return all(a[i] > a[i + 1] for i in xrange(len(a) - 1))


def hanoi_move(n, a, b, c, board):
  """Move n pegs from positions `a` to `b` using `c` as intermediary.
  
  Assumes that n pegs in correct order on `a` and that any other pegs on board
  have discs >= n - 1 or are empty.

  Args:
    n: Number of pegs to move
    a: From peg
    b: To peg
    c: Intermediary peg
    board: Array of length three with disc configuration
  """

  if not all(_is_reverse_sorted(x) for x in board):
    raise ValueError("Board is not legal.")

  if n == 1:
    # Base case: move one peg
    board[b].append(board[a].pop())
    return

  hanoi_move(n - 1, a, c, b, board)
  hanoi_move(1, a, b, c, board)
  hanoi_move(n - 1, c, b, a, board)
  return


def permutations(a):
  """Compute all permutations of array.
  
  Time complexity: O(n * n!)
  Space complexity: O(1)
  """

  perms = []
  permutations_helper(0, a, perms)
  return perms


def permutations_helper(i, curr, perms):
  if i == len(curr) - 1:
    perms.append(curr[:])
    return

  for j in range(i, len(curr)):
    curr[i], curr[j] = curr[j], curr[i]
    permutations_helper(i + 1, curr, perms)
    curr[j], curr[i] = curr[i], curr[j]

  return


def permutations_nr(a):
  perms = [a]

  for i in range(len(a) - 1):
    new_perms = []
    for j in range(i + 1, len(a)):
      for p in perms:
        new_perm = p[:]
        new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
        new_perms.append(new_perm)
    perms.extend(new_perms)

  return perms


def all_subsets(a, k):
  """Construct all subsets of size k from array.
  
  NOTE: This code requires memoization to be efficient.
  """

  subsets = []
  all_subsets_helper(a, k, len(a), subsets)
  return subsets


def all_subsets_helper(a, k, n, subsets):
  # Base cases: subset of one item or n == k
  if k <= 1:
    for i in range(n):
      subsets.append(set([a[i]]))
    return
  elif n <= 1 or n <= k:
    subsets.append(set(a[:k]))
    return

  all_subsets_helper(a, k, n - 1, subsets)
  new_sets = []
  all_subsets_helper(a, k - 1, n - 1, new_sets)
  for s in new_sets:
    s.add(a[n - 1]) 
  subsets.extend(new_sets)
  return


def is_palindrome(s):
  return all(s[i] == s[~i] for i in range(len(s) // 2))


def palindrome_decomps(s):
  """Return all palindromic decompositions of string s.
  
  NOTE: This requires memoization to be efficient.
  """

  return pal_helper(0, s)


def pal_helper(pos, s):
  if pos == len(s):
    return [[]] 

  ret = []
  for i in range(pos, len(s)):
    if is_palindrome(s[pos: i + 1]):
      ret.extend([s[pos: i + 1]] + decomp for decomp in pal_helper(i + 1, s))
  return ret


def palindrome_decomps2(s):
  """Write function in EPI style."""

  ret = []
  pal_helper2(0, [], s, ret)
  return ret


def pal_helper2(pos, decomp, s, ret):
  if pos == len(s):
    ret.append(decomp)

  for i in range(pos, len(s)):
    if is_palindrome(s[pos: i + 1]):
      pal_helper2(i + 1, decomp + [s[pos: i + 1]], s, ret)

  return
