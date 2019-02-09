"""BST problems: the workhorse of data structures!"""
import tree
import collections

class BST(tree.BinaryTree):
  def is_valid(self):
    """Checks BST property on tree.
    
    If true, inorder traversal should yield sorted data.

    Time: O(N)
    Space: O(H)

    Returns:
      Bool with validity status
    """

    it = self.inorder_generator()
    prev, val = next(it, None), next(it, None)
    while val:
      if val < prev:
        return False
      prev = val
      val = next(it, None)
    return True

  def search(self, value):
    """Search BST for value, returning False if not found.
    
    Returns:
      Node if value present, else None.
    """

    return self.search_helper(self.root, value)

  def search_helper(self, node, value):
    if not node:
      return None
    if node.data == value:
      return node
    if node.data > value:
      return self.search_helper(node.left, value)
    if node.data < value:
      return self.search_helper(node.right, value)

  def min_k(self, k):
    """Returns min k nodes from tree.
    
    Time complexity: O(H + K), H to descend to min and K traversals
    Space complexity: O(1)
    """

    traversal = []
    self.min_k_helper(self.root, k, traversal)
    return traversal

  def min_k_helper(self, node, k, traversal):
    # Base case: empty node or traversal already complete
    # Adding traversal length stops O(N) exploration of remaining tree
    if not node or len(traversal) >= k:
      return

    self.min_k_helper(node.left, k, traversal)

    if len(traversal) < k:
      traversal.append(node.data)

    self.min_k_helper(node.right, k, traversal)
    
    return

  def max_k(self, k):
    """Returns max k nodes from tree.
    
    Time complexity: O(H + K)
    Space complexity: O(1)
    """
    """Returns max k nodes from tree."""

    traversal = []
    self.max_k_helper(self.root, k, traversal)
    return traversal

  def max_k_helper(self, node, k, traversal):
    if not node or len(traversal) >= k:
      return

    self.max_k_helper(node.right, k, traversal)

    if len(traversal) < k:
      traversal.append(node.data)

    self.max_k_helper(node.left, k, traversal)

    return

  def insert(self, value):
    """Insert value into BST."""

    if not self.root:
      self.root = tree.Node(value)
    else:
      self.insert_helper(self.root, value)
    return

  def insert_helper(self, node, value):
    if node.data == value:
      return
    elif node.data > value:
      if not node.left:
        node.left = tree.Node(value)
        node.left.parent = node
      else:
        self.insert_helper(node.left, value)
    else:
      if not node.right:
        node.right = tree.Node(value)
        node.right.parent = node
      else:
        self.insert_helper(node.right, value)
    return

  def _max_node(self, node):
    """Return the max node of subtree starting from node."""

    if not node:
      return None
    while node.right:
      node = node.right
    return node

  def _min_node(self, node):
    """Return the min node of subtree starting from node."""

    if not node:
      return None
    while node.left:
      node = node.left
    return node

  def delete(self, value):
    node = self.search(value)
    if not node:
      raise ValueError("Value not present in tree.")
    self.delete_helper(node)

  def delete_helper(self, node):
    if node.right:
      # One or two children
      min_right = self._min_node(node.right)
      node.data = min_right.data
      self.delete_helper(min_right)
    elif node.left:
      # Left child only
      max_left = self._max_node(node.left)
      node.data = max_right.data
      self.delete_helper(max_left)
    else:
      # Base case: leaf node
      if not node.parent:
        # Deleting the root node
        self.root = None
        return
      if node == node.parent.left:
        node.parent.left = None
      else:
        node.parent.right = None
    return


class PageVisitRanker(object):
  """Tabulates most visited pages from stream of page data.

   Optimized to return most visited ranking at any point in stream.
   """

  def __init__(self):
    self._bst = BST()
    self._map = collections.Counter()

  def add_page_visit(self, id):
    """Increment visit count for page.

    Time complexity: O(H)
    Space complexity: O(1)
    """

    curr_count = self._map[id]
    self._map[id] += 1
    if curr_count > 0:
      self._bst.delete((curr_count, id))
    self._bst.insert((curr_count + 1, id))
    return

  def add_page_visits(self, ids):
    for id in ids:
      self.add_page_visit(id)

  def top_visited_pages(self, k):
    """Compute top visited pages at current counts.

    Time complexity: O(H + k)
    Space complexity: O(1)

    Args:
      k: Number of pages in ranking

    Returns:
      List of page ids in order of visit counts.
    """

    return [x[1] for x in self._bst.max_k(k)]
