import copy

def towers_of_hanoi(n):
  """Provide list of moves to solve ToH with n plates."""
  # Set up game with stacks
  game = [range(n - 1, -1, -1), [], []]
  moves = []
  _toh_helper(n, game, moves, 0, 1, 2)
  return moves, game

def _toh_mover(game, moves, from_peg, to_peg):
  """Makes and records move in ToH game."""
  moved = game[from_peg].pop()
  if game[to_peg] and game[to_peg][-1] < moved:
    raise StandardError("Cannot place larger plate " + str(moved) +
                        " on smaller plate " + str(game[to_peg][-1]))
  game[to_peg].append(moved)
  moves.append((moved, from_peg, to_peg))

def _toh_helper(n, game, moves, from_peg, to_peg, use_peg):
  # Base case: two smallest pegs (can be moved anywhere)
  if n > 0:
    _toh_helper(n - 1, game, moves, from_peg, use_peg, to_peg)
    _toh_mover(game, moves, from_peg, to_peg)
    _toh_helper(n - 1, game, moves, use_peg, to_peg, from_peg)

def all_permutations(a):
  """Generate all permutations of array.
  Time complexity: O(N * N!) since N! permutations and have to make fresh copy 
  of array each time.
  """
  ret = []
  _all_perm_helper(a, 0, ret)
  return ret

def _all_perm_helper(perm, i, ret):
  """Find all permutations of array from position i.
  Args:
    perm: Array to be permuted
    i: Position from which to start permutation
    ret: list of results
  """
  if i == len(perm):
    ret.append(perm)
  for j in range(i, len(perm)):
    new_perm = perm[:]
    new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
    _all_perm_helper(new_perm, i + 1, ret)
  return

def power_set(s):
  """Generate list of sets in power set of s."""
  ret = [set()]
  _power_set_helper(s, ret)
  return ret

def _power_set_helper(s, ret):
  """Power set is union of all sets that include item and those that do not."""
  if not s:
    return
  # Make copy of set and remove an item
  new_set = copy.deepcopy(s)
  next_item = next(iter(s))
  new_set.remove(next_item)
  # Add subsets without item to ret
  _power_set_helper(new_set, ret)
  # Add union of item with subsets without it to ret
  ret_extend = []
  for i in range(len(ret)):
    l = copy.deepcopy(ret[i])
    l.add(next_item) 
    ret.append(l)
  return

def all_subsets_k(s, k):
  """Return all subsets of size k from s.

  Time complexity: O(choose(n, k) * n)
  
  Args:
    s: Set from which to choose items
    k: Size of subsets
  Returns:
    List of sets
  """
  if k == 1:
    return [{x} for x in s]
  if k == len(s):
    return [s]
  # Next item to remove from set
  next_item = next(iter(s))
  s_without = copy.deepcopy(s)
  s_without.remove(next_item)
  all_sets_without = all_subsets_k(s_without, k)
  all_sets_with = all_subsets_k(copy.deepcopy(s_without), k - 1)
  for r in all_sets_with:
    r.add(next_item)
  return all_sets_without + all_sets_with

def n_queens(n):
  """Return all non-attacking configurations of n queens on an nxn chessboard.

  Args:
    n: size of chessboard
  Returns:
    Array of arrays of length n indicating column position of queen in row i
  """
  ret = []
  _n_queens_helper(1, n, [0] * n, ret)
  return ret

def _n_queens_helper(i, n, board, ret):
  """Checks all legal configurations for row i given the current board.
  
  Args:
    i: current row
    n: size of board
    board: array of length n giving column position of queen in row
    ret: array to store complete answers
  """
  if i >= n + 1:
    ret.append(board)
  for j in range(1, n + 1):
    # Consider all possible column positions j in [1, ..., n]
    legal = True
    for p in range(1, i):
      # Check if any queens in rows before 'i' can attack
      if ((j == board[p - 1]) or  # Same column
          (j == board[p - 1] + (i - p)) or  # Diagonal to the right 
          (j == board[p - 1] - (i - p))):  # Diagonal to the left
        legal = False
        continue
    if legal:
      # If legal move, try to fill in rest of the board
      new_board = board[:]
      new_board[i - 1] = j 
      _n_queens_helper(i + 1, n, new_board, ret)
