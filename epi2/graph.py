"""Graph problems."""
import collections
import heapq

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

def _path_from_path_dict(path_dict, start, end):
  """Recover traversal from path_dict."""

  path = [end]
  curr = end
  while curr != start:
    curr = path_dict[curr]
    path.append(curr)
  return path[::-1]


def shortest_maze_traversal(start, end, maze):
  """Find the shortest path between start and end of maze.

  Args:
    start, end: Coordinate objects indicating start and end points.
    maze: Square, 2D boolean array where ones are open and zeros blocked squares
  """
  
  queue = collections.deque([start])
  path_dict = {start : None}
  curr = None

  while queue:
    curr = queue.popleft()

    if curr == end:
      # Path found: return it 
      return _path_from_path_dict(path_dict, start, end)
  
    for pos in [
        Coordinate(curr.x + 1, curr.y),
        Coordinate(curr.x, curr.y + 1),
        Coordinate(curr.x - 1, curr.y),
        Coordinate(curr.x, curr.y - 1)]:
      if any(p < 0 or p >= len(maze) for p in pos) or maze[pos.x][pos.y] == 0:
        continue
      # Mark position as visited
      maze[curr.x][curr.y] = 0
      # Mark origin of point
      path_dict[pos] = curr
      queue.append(pos)

  # No path: return None 
  return None


def maze_traversal_dfs(start, end, maze):
  """Return path between maze start and end using DFS.
  
  If no path, return None.
  """

  path = []
  if maze_traversal_dfs_helper(start, end, maze, path):
    return path
  return None


def maze_traversal_dfs_helper(start, end, maze, path):

  # Add self to path
  path.append(start)

  # Base case: at end point
  if start == end:
    return True

  # Mark current point as visited
  maze[start.x][start.y] = 0

  for pos in [
      Coordinate(start.x + 1, start.y),
      Coordinate(start.x, start.y + 1),
      Coordinate(start.x - 1, start.y),
      Coordinate(start.x, start.y - 1)]:
    if any(p < 0 or p >= len(maze) for p in pos) or maze[pos.x][pos.y] == 0:
      continue
    if maze_traversal_dfs_helper(pos, end, maze, path):
      return True

  # Remove self fromp path, hit dead end
  path.pop()
  return False


def is_maze_path(start, end, maze):
  """Determine if there is a path between maze start and end."""

  # Base case: at end point
  if start == end:
    return True

  # Mark current point as visited
  maze[start.x][start.y] = 0

  for pos in [
      Coordinate(start.x + 1, start.y),
      Coordinate(start.x, start.y + 1),
      Coordinate(start.x - 1, start.y),
      Coordinate(start.x, start.y - 1)]:
    if any(p < 0 or p >= len(maze) for p in pos) or maze[pos.x][pos.y] == 0:
      continue
    if is_maze_path(pos, end, maze):
      return True

  # Hit bottom of stack without finding end
  return False


def closest_XY_pair(a):
  """Return Manhattan distance of closest 'x' in 'y' in 2d array.

  Args:
    a: 2d array with lowercase chars

  Returns:
    Distance of closest 'x' and 'y'.
  """

  nrow, ncol = len(a), len(a[0])
  queue = collections.deque([
    Coordinate(i, j) for i in range(nrow) for j in range(ncol) 
    if a[i][j] == 'x'])
  dists = {x : 0 for x in queue}

  while queue:
    start = queue.popleft()
    dist = dists[start]

    for pos in [
        Coordinate(start.x + 1, start.y),
        Coordinate(start.x, start.y + 1),
        Coordinate(start.x - 1, start.y),
        Coordinate(start.x, start.y - 1)]:
      if (pos.x < 0 or pos.y < 0 or pos.x >= nrow or pos.y >= ncol or 
          pos in dists):
        continue
      dists[pos] = dist + 1
      if a[pos.x][pos.y] == 'y':
        # First 'y' found always the closest
        return dists[pos]
      queue.append(pos)

  # No 'y' in a
  return None


class SimpleGraph(object):
  def __init__(self, adj_list=None):
    self.adj_list = adj_list or dict()

  def add_vertex(self, vertex, edge_list):
    self.adj_list[vertex] = edge_list

  def is_connected(self, source, dest):
    """Return True if path from source to dest node."""

    visited = set()
    return self.is_connected_helper(source, dest, visited)

  def is_connected_helper(self, source, dest, visited):
    if source == dest:
      return True

    visited.add(source)

    for edge in self.adj_list[source]:
      if edge in visited:
        continue
      if self.is_connected_helper(edge, dest, visited):
        return True

    # Hit bottom of stack without finding dest
    return False

  def dfs_path(self, source, dest):
    """Return DFS path from source to destination; None if not connected."""
    pass

  def is_cyclic(self):
    """Return True if cycle in graph."""

    # Track colors of nodes. Black nodes are in neither set.
    # Do not need to track black nodes because are complement of (white, grey) 
    white = set(self.adj_list.keys()) 
    grey = set() 
    while white:
      if self.is_cyclic_helper(white.pop(), white, grey):
        return True
    return False

  def is_cyclic_helper(self, node, white, grey):
    white.discard(node)
    grey.add(node)
    for edge in self.adj_list[node]:
      if edge in grey:
        return True
      if edge in white:
        if self.is_cyclic_helper(edge, white, grey):
          return True
    grey.remove(node)
    return False

  def topological_sort(self):
    """Perform topological sort of nodes.

    Note that for topological sort forests are allowed but cycles are not.

    Returns:
      List of nodes names in sorted order

    Raises:
      ValueError: Graph is cyclic.
    """
    
    if self.is_cyclic():
      raise ValueError("Graph is cyclic.")

    white = set(self.adj_list.keys())
    ret = []
    while white:
      self.topological_helper(white.pop(), white, ret)
    ret.reverse()
    return ret

  def topological_helper(self, node, white, ret):
    white.discard(node)

    for edge in self.adj_list[node]:
      if edge in white:
        self.topological_helper(edge, white, ret)

    # Add node to ret once black (processed)
    ret.append(node)

  def shortest_path(self, source, dest):
    """Find the shortest path between the source and destination nodes.
    
    Returns None if no connection.
    """

    queue = collections.deque([source])
    path_dict = {source: None}
    visited = set(source)
  
    while queue:
      curr = queue.popleft()

      if curr == dest:
        return _path_from_path_dict(path_dict, source, dest)

      for edge in self.adj_list[curr]:
        if edge not in visited:
          # Mark position as visited
          # Need to add visited indicator here so can't add to queue twice
          visited.add(edge)
          path_dict[edge] = curr
          queue.append(edge)

    # If queue empty without hitting dest, not connected
    return None


Edge = collections.namedtuple('Edge', ['source', 'dest', 'weight'])


class Graph(object):
  def __init__(self, adj_list=None):
    self.adj_list = adj_list or dict()


def min_span_tree(graph):
  """Return set of edges that connect nodes in graph with minimum cost.

  Uses Prim's algorithm.

  Time complexity: O(|E| log |E|)
  Space complexity: O(|E|)

  Args:
    graph: A Graph object

  Returns:
    A list of Edge objects
  """

  start = next(iter(graph.adj_list))
  visited = set()
  edges = set()
  heap = [(0, Edge(None, start, 0))]
  while heap:
    # Add dest to network if not already visited
    _, edge = heapq.heappop(heap)
    if edge.dest in visited:
      continue
    visited.add(edge.dest)
    if edge.source is not None:
      edges.add(edge) 
    for outedge in graph.adj_list[edge.dest]:
      heapq.heappush(heap, (outedge.weight, outedge))
  return edges
