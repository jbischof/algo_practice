import binary_tree as bt

class BST(bt.BinaryTree):
  def check_valid(self):
    """ Verifies binary tree has BST property using inorder traversal.
    If tree is BST, inorder should produce keys in sorted order.
    Time complexity: O(N) (each node traversed once)
    Space complexity: O(1) """
    # Empty tree trivially satisfies property
    if not self.root:
      return True
    return self.check_valid_helper(self.root, None)

  def check_valid_helper(self, node, prev):
    """ Helper function for recursive validity check """
    if node.left and not self.check_valid_helper(node.left, prev):
      return False
    if prev and node.value < prev.value:
      return False
    # Now this node is the most recent
    prev = node
    if node.right and not self.check_valid_helper(node.right, prev):
      return False
    return True

  def search(self, value):
    """ Search for value in BST.
    Args:
      value: Value to find
    Returns:
      Boolean
    Time Complexity: O(H), where H is height of tree
    Space Complexity: O(1) """
    return self.search_helper(self.root, value)

  def search_helper(self, node, value):
    if value == node.value:
      return True
    if value < node.value:
      if not node.left:
        return False
      return self.search_helper(node.left, value)
    if value > node.value:
      if not node.right:
        return False
      return self.search_helper(node.right, value)

  def next_largest(self, value):
    """ Search for next largest value in BST.
    Args:
      value: baseline value
    Returns:
      Value or None if 'value' larger than entire tree      
    Time Complexity: O(H), where H is height of tree
    Space Complexity: O(1) """
    return self.next_largest_helper(self.root, value, None)

  def next_largest_helper(self, node, value, last_largest):
    if value < node.value:
      last_largest = node.value
      if not node.left:
        return last_largest 
      return self.next_largest_helper(node.left, value, last_largest)
    if value >= node.value:
      if not node.right:
        return last_largest
      return self.next_largest_helper(node.right, value, last_largest)
