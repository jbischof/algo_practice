"""Adventures in graphs."""
import collections
import string


def maze_traverse_shortest(maze):
  """Find shortest path through maze from start to finish.

  Uses BFS path through graph interpretation of maze. Neighboring white
  squares are connected and all other vertices are not.
  Time compexity: O(|V|), where V is the set of white squares.
  Space compexity: O(|V|), maximium length of queue.
  
  Args:
    maze: An n x m binary array where zeros are blocked squares and ones are
          open squares. Start is assumed to be (n - 1, 0) and end is (0, m - 1).
  Returns:
    List of moves pertaining to shortest path, or None if there is no path.
  """

  n, m = len(maze), len(maze[0])
  i, j, = n - 1, 0
  queue = collections.deque()
  queue.append((i, j))
  paths_from = {(i, j): None}
  path = []

  while queue: 
    maze[i][j] = 0
    if i == 0 and j == m - 1:
      # Got to the end, return the path
      path.append((i, j))
      while paths_from[(i, j)]: 
        i, j = paths_from[(i, j)]
        path.append((i, j))
      path.reverse()
      return path
    for new_i, new_j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
      if (new_i <= n - 1 and new_i >= 0 and new_j <= m - 1 and new_j >= 0
          and maze[new_i][new_j]):
        queue.append((new_i, new_j))
        paths_from[(new_i, new_j)] = (i, j)
    i, j = queue.popleft()

  # Never got to the end
  return None


def flood_fill(mat, start):
  """Change color of connected region of white squares of binary matrix.

  Uses DFS to find entries of matrix connected to starting position, where
  connection means adjacent and same color.

  Time compexity: O(|V|), where V is the set of squares of the same color.
  Space compexity: O(|V|), maximium size of stack.
  
  Args:
    mat: An n x m binary array where zeros and one indicate black and white 
         colors, respectively.
    start: Tuple of starting coordinates in matrix.
  Returns:
    The same array with the indicated region flood-filled. 
  """

  n, m = len(mat), len(mat[0])
  i, j, = start
  stack = [(i, j)]

  while stack: 
    mat[i][j] = 0
    for new_i, new_j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
      if (new_i <= n - 1 and new_i >= 0 and new_j <= m - 1 and new_j >= 0
          and mat[new_i][new_j]):
        stack.append((new_i, new_j))
    i, j = stack.pop()

  return mat


def string_path_transform(a, b, str_set):
  """Return shortest path transformation between strings if possible.
  
  Given dictionary of strings, find shortest path to change string 'a' to 'b' 
  changing only one letter at a time.
  Time complexity: O(N * L), where N number of words and L = len(a)
  Space complexity: O(N), maximum length of queue
  Args:
    a, b: strings
    str_set: set of strings that can be used in traversal
  Returns:
    Array giving shortest path of words or None if not possible
  """

  path = [b]
  paths_from = {a: None}
  queue = collections.deque()
  queue.append(a)
  curr = a
  # Make sure a and b are in set
  str_set.update([a, b])

  while queue:
    str_set.discard(curr)
    if curr == b:
      while paths_from[curr]:
        curr = paths_from[curr]
        path.append(curr)
      path.reverse()
      return path
    for j in range(len(a)):
      for char in string.ascii_lowercase:
        candidate = curr[:j] + char + curr[(j+1):]
        if candidate in str_set:
          paths_from[candidate] = curr
          queue.append(candidate)
    curr = queue.popleft()

  return None
