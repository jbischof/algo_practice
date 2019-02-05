"""Traversing through the trees."""

class Node(object):
  def __init__(self, data, left=None, right=None, parent=None):
    self.data = data
    self.left = left
    self.right = right
    self.parent = parent
    self.visited = False


class BinaryTree(object):
  def __init__(self, root=None):
    self.root = root

  def preorder(self):
    """Return preorder traversal of tree."""

    traversal = []
    self.preorder_helper(self.root, traversal)
    return traversal

  def preorder_helper(self, node, traversal):
    # Base case: node is empty
    if not node:
      return

    traversal.append(node.data)
    self.preorder_helper(node.left, traversal)
    self.preorder_helper(node.right, traversal)
    return

  def inorder(self):
    """Return inorder traversal of tree."""

    traversal = []
    self.inorder_helper(self.root, traversal)
    return traversal

  def inorder_helper(self, node, traversal):
    # Base case: node is empty
    if not node:
      return

    self.inorder_helper(node.left, traversal)
    traversal.append(node.data)
    self.inorder_helper(node.right, traversal)
    return

  def inorder_generator(self):
    """Return inorder traversal of tree in generator form."""

    for val in self.inorder_helper_generator(self.root):
      yield val

  def inorder_helper_generator(self, node):
    # Base case: node is empty
    if not node:
      return

    for val in self.inorder_helper_generator(node.left):
      yield val

    yield(node.data)

    for val in self.inorder_helper_generator(node.right):
      yield val

    return


  def inorder_no_recursion(self):
    """Inorder recursion with explicit stack.
    
    Time: O(N)
    Space: O(H), or O(N) if count visited bools.

    Returns:
      List of traversal data.
    """

    traversal, stack = [], []
    stack.append(self.root)

    while stack:
      node = stack.pop()
      if node.right and not node.right.visited:
        stack.append(node.right)
        node.right.visited = True
      if not node.left or node.left.visited:
        # Only append if left side empty or visited
        traversal.append(node.data)
        node.visited = True
      elif node.left:
        stack.extend([node, node.left])

    return traversal

  def inorder_no_recursion_generator(self):
    """Inorder recursion with explicit stack.
    
    Time: O(N)
    Space: O(H), or O(N) if count visited bools.

    Returns:
      Generator for traversal data
    """

    stack = []
    stack.append(self.root)

    while stack:
      node = stack.pop()
      if node.right and not node.right.visited:
        stack.append(node.right)
        node.right.visited = True
      if not node.left or node.left.visited:
        # Only append if left side empty or visited
        yield node.data
        node.visited = True
      elif node.left:
        stack.extend([node, node.left])

    return

  def postorder(self):
    """Return postorder traversal of tree."""

    traversal = []
    self.postorder_helper(self.root, traversal)
    return traversal

  def postorder_helper(self, node, traversal):
    # Base case: node is empty
    if not node:
      return

    self.postorder_helper(node.left, traversal)
    self.postorder_helper(node.right, traversal)
    traversal.append(node.data)
    return

  def is_height_balanced(self):
    """Determines if for each subtree height of left and height differ <= 1."""

    return self.is_height_balanced_helper(self.root)[0]

  def is_height_balanced_helper(self, node):
    """Recursive function to check if subtree starting at node is balanced."""
    
    # Base case: node is empty
    if not node:
      return True, 0
    
    # Left side
    is_bal_left, height_left = self.is_height_balanced_helper(node.left)
    # Right side
    is_bal_right, height_right = self.is_height_balanced_helper(node.right)

    if (not is_bal_left or not is_bal_right or 
        abs(height_left - height_right) > 1):
      return False, 0
    else:
      return True, max(height_left, height_right) + 1

  def has_path_sum(self, k):
    """Check if integer-value data sum to `k` along path from root to leaf."""

    return self.has_path_sum_helper(self.root, k)

  def has_path_sum_helper(self, node, k):
    # Base case: empty node:
    if not node:
      return False

    # Subtract node value from remaining sum
    k -= node.data

    # Only check sum if leaf node
    if not node.left and not node.right:
      return k == 0 

    return (self.has_path_sum_helper(node.left, k) or
            self.has_path_sum_helper(node.right, k)) 

