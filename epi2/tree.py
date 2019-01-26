"""Traversing through the trees."""

class Node(object):
  def __init__(self, data, left=None, right=None, parent=None):
    self.data = data
    self.left = left
    self.right = right
    self.parent = parent


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

    if node.left:
      self.preorder_helper(node.left, traversal)

    if node.right:
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

    if node.left:
      self.inorder_helper(node.left, traversal)

    traversal.append(node.data)

    if node.right:
      self.inorder_helper(node.right, traversal)

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

    if node.left:
      self.postorder_helper(node.left, traversal)

    if node.right:
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

