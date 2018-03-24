"""Tree and graph problems."""

import collections 


class Graph(object):
  """Directed graph based on adjacency list."""

  def __init__(self, adj_dict=None):
    """Initialize graph.
    
    Args:
      adj_dict: A dict mapping string names to list of string connections. 
    """

    self.adj_dict = adj_dict or {}

  def isConnected(self, node1, node2):
    """Returns True is nodes are connected in graph, else False.
    
    Args:
      node1, node2: Names of source and destination nodes.
    Returns:
      Boolean.
    """

    visited = set()
    queue = collections.deque()
    queue.append(node1)
    while queue:
      curr = queue.popleft()
      visited.add(curr)
      for node in self.adj_dict[curr]:
        if node == node2:
          return True
        if not node in visited:
          queue.append(node)
    return False


class Node(object):
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None


class Tree(object):
  def __init__(self, root=None):
    self.root = root

  @classmethod
  def from_sorted_list(cls, a):
    """Construct balanced Tree from sorted list of values."""

    return cls(from_sorted_list_helper(a))

  def inorder(self):
    """Return inorder traversal of tree."""

    ret = []
    self.inorder_helper(self.root, ret)
    return ret

  def inorder_helper(self, node, ret):
    """Recursive function to compute inorder traversal."""

    if not node:
      return
    self.inorder_helper(node.left, ret) 
    ret.append(node.value)
    self.inorder_helper(node.right, ret) 

  def bfs(self):
    """Returns BFS of tree.
    
    Time complexity: O(N) for traversal
    Space complexity: O(2^(H-1)) for holding lowest level of complete tree
        in queue. This is significantly more than DFS, which has a worst case of
        O(H).
    """
    
    ret = []
    queue = collections.deque()
    if self.root:
      queue.append(self.root)
    while queue:
      current = queue.popleft()
      ret.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
    return ret

  def level_lists(self):
    """Write tree values into separate list for each level.
    
    Time complexity: O(N)
    Space complexity: O(H)
    """

    ret = []
    self.level_lists_helper(self.root, 0, ret)
    return ret

  def level_lists_helper(self, node, level, ret):
    """Recursive function to compute level lists."""

    if not node:
      return
    if len(ret) < level + 1:
      ret.append([])
    ret[level].append(node.value)
    self.level_lists_helper(node.left, level + 1, ret) 
    self.level_lists_helper(node.right, level + 1, ret) 

  def is_balanced(self):
    """Returns True if height of any two subtrees differs by more than one."""

    return self.is_balanced_helper(self.root)[1]

  def is_balanced_helper(self, node):
    """Recursive function to check subtree balance.

    Returns:
      Tuple of (depth, isBalanced) of subtree starting with node
    """

    # Base case: empty node
    if not node:
      return 0, True
    left_depth, left_bal = self.is_balanced_helper(node.left)
    right_depth, right_bal = self.is_balanced_helper(node.right)
    node_bal = abs(left_depth - right_depth) <= 1
    tree_depth = max(left_depth, right_depth) + 1
    if not (left_bal and right_bal and node_bal):
      return tree_depth, False
    return tree_depth, True

  def is_bst(self):
    """Check if tree is BST.
    
    Time complexity: O(N)
    Space complexity: O(H)
    """

    return self.is_bst_helper(self.root, float('-Inf'), float('Inf')) 

  def is_bst_helper(self, node, min_enforce, max_enforce):
    if not node:
      return True
    if not (min_enforce <= node.value < max_enforce):
      return False
    return (self.is_bst_helper(node.left, min_enforce, node.value) and
        self.is_bst_helper(node.right, node.value, max_enforce))

  def inorder_successor(self, node):
    """Return the inorder successor to node on tree.
    
    Assuming parent links.

    Time complexity: O(log N) since may need to ascend entire tree
    Space complexity: O(1)
    """

    if node.right:
      return node.right
    # Otherwise need to find a left child and return its parent
    while not node.parent.left is node:
      # If parent is the root coming from the right, already at greatest node
      if node.parent is self.root:
        return None
      node = node.parent
    return node.parent

  def __eq__(self, other):
    """Check if two trees are equal."""
    return self.eq_helper(self.root, other.root)

  def __ne__(self, other):
    """Check if two trees are not equal."""
    return not self.eq_helper(self.root, other.root)

  def eq_helper(self, node_self, node_other):
    """Recursive function to compare trees at one position."""
    # Empty trees are equal
    if not node_self and not node_other:
      return True
    # One node empty when other is not means not equal
    if (not node_self and node_other) or (node_self and not node_other):
      return False
    # Compare values if both exist
    if not (node_self.value == node_other.value):
      return False
    # Recurse on children if both exist and equal values
    return (
        self.eq_helper(node_self.left, node_other.left) and 
        self.eq_helper(node_self.right, node_other.right)) 

  def has_subtree(self, other):
    """Returns true if `other` is a subtree.
    
    Time complexity: O(|self| * |other|)
    Space complexity: O(log|self| + log|other|)

    However, average time complexity likely much lower than worst case. If root
    of subtree occurs k << |other| times then time complexity is 
    O(|self| + k|other|).
    """

    return self.has_subtree_helper(self.root, other)

  def has_subtree_helper(self, node, other):
    """Recursive function to look for subtree `other`."""
    if not node:
      return False
    if Tree(node) == other:
      return True
    return (
        self.has_subtree_helper(node.left, other) or
        self.has_subtree_helper(node.right, other))

    
def from_sorted_list_helper(a):
  """Returns the median value in a sorted list as a Node, or None if empty.

  Populates children nodes recursively.
  
  Args:
    a: A sorted list of values.
  Returns:
    A Node object.
  """

  if not a:
    return None
  midpoint = len(a) // 2
  root = Node(a[midpoint])
  root.left = from_sorted_list_helper(a[ :midpoint])
  root.right = from_sorted_list_helper(a[(midpoint + 1): ])
  return root 


def build_order(jobs, depend_pairs):
  """Determine build order for jobs with dependencies (if feasible).

  This algorithm known as `topological sort`.

  Time complexity: O(|V| + |E|)
  Space complexity: O(|V| + |E|)

  Args:
    jobs: List of names of jobs to be performed
    depend_pairs: Nested list of 2-tuples giving (dependency_job, job) pairs.
  Returns:
    Build order list or `None` if no feasible build order.
  """

  build_order = []
  inbound_adj_dict = {}
  outbound_adj_dict = {}
  # Get dictionaries of inbound and outbound links
  for job in jobs:
    inbound_adj_dict[job] = set()
    outbound_adj_dict[job] = set()
  for pair in depend_pairs:
    inbound_adj_dict[pair[1]].add(pair[0])
    outbound_adj_dict[pair[0]].add(pair[1])
  # Get list of nodes without dependencies
  depend_free_jobs = set()
  remain_jobs = set(jobs)
  for job, dep_set in inbound_adj_dict.iteritems():
    if not dep_set:
      remain_jobs.remove(job)
      depend_free_jobs.add(job)
  while depend_free_jobs:
    depend_job = depend_free_jobs.pop()
    build_order.append(depend_job)
    for job in outbound_adj_dict[depend_job]:
      # Remove depend_job from inbound deps of job
      inbound_adj_dict[job].remove(depend_job)
      # If no more dependencies, move to depend_free_jobs
      if not inbound_adj_dict[job]:
        remain_jobs.remove(job)
        depend_free_jobs.add(job)
  # If still jobs in inbound_adj_dict, not feasible
  if remain_jobs:
    return None
  return build_order


