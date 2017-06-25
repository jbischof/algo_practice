class Node():
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None

class BinaryTree():
  def __init__(self, root=None):
    self.root = root

  def preorder(self):
    """ Returns pre-order traversal of tree """
    ret = []
    self.preorder_helper(ret, self.root)
    return ret

  def preorder_helper(self, ret, node):
    if node:
      ret.append(node.value)
    if node.left:
      self.preorder_helper(ret, node.left)
    if node.right:
      self.preorder_helper(ret, node.right)
    return

  def inorder(self):
    """ Returns in-order traversal of tree """
    ret = []
    self.inorder_helper(ret, self.root)
    return ret

  def inorder_helper(self, ret, node):
    if node.left:
      self.inorder_helper(ret, node.left)
    if node:
      ret.append(node.value)
    if node.right:
      self.inorder_helper(ret, node.right)
    return

  def postorder(self):
    """ Returns post-order traversal of tree """
    ret = []
    self.postorder_helper(ret, self.root)
    return ret

  def postorder_helper(self, ret, node):
    if node.left:
      self.postorder_helper(ret, node.left)
    if node.right:
      self.postorder_helper(ret, node.right)
    if node:
      ret.append(node.value)
    return

  def level_print(self):
    """ Return list of lists of nodes in tree. Each list contains items from one
    level in left-to-right order """
    ret = []
    level = 0
    self.level_print_helper(self.root, ret, level)
    return ret

  def level_print_helper(self, node, ret, level):
    if node:
      # Append extra level to return object if too short
      if len(ret) - level < 1:
        ret.append([])
      ret[level].append(node.value)
    if node.left:
      self.level_print_helper(node.left, ret, level + 1)
    if node.right:
      self.level_print_helper(node.right, ret, level + 1)
    return

  def is_height_balanced(self):
    """ Checks if all left/right subtrees do not differ more than one level
    in height """
    is_bal, _ = self.is_height_balanced_helper(self.root)
    return is_bal

  def is_height_balanced_helper(self, node):
    left_depth, right_depth = 0, 0
    left_bal, right_bal = True, True
    is_bal = True
    if node.left:
      left_bal, left_depth = self.is_height_balanced_helper(node.left)
      left_depth += 1
    if node.right:
      right_bal, right_depth = self.is_height_balanced_helper(node.right)
      right_depth += 1
    if not left_bal or not right_bal or abs(left_depth - right_depth) > 1:
      is_bal = False
    return is_bal, max(left_depth, right_depth)

  def is_symmetric(self):
    """ Checks if left and right subtrees are mirror images """
    if not self.root:
      return True
    return self.is_symmetric_helper(self.root.left, self.root.right)

  def is_symmetric_helper(self, left_node, right_node):
    """ Compares left and right subtrees for equality recursively """
    # Case 1: both nodes empty
    if not left_node and not right_node:
      return True
    # Case 2: one node empty but not the other
    if not left_node or not right_node:
      return False
    # Case 3: both have data
    return (left_node.value == right_node.value and 
        self.is_symmetric_helper(left_node.left, right_node.right) and
        self.is_symmetric_helper(left_node.right, right_node.left))

  def get_ancestry(self, node):
    """ Return list of ancestors of node. Only works if parent field is 
    populated """
    # TODO(bischof): just need to return depth to avoid O(N) storage
    res = []
    while node.parent:
      res.append(node.parent)
      node = node.parent
    return res

  def least_common_ancestor(self, node1, node2):
    """ Find the least common ancestor of two nodes. Only works if parent field 
    is populated. """
    # Find ancestry of both nodes
    ancestor1 = self.get_ancestry(node1)
    ancestor2 = self.get_ancestry(node2)
    # Want first array to be smaller
    if len(ancestor1) > len(ancestor2):
      ancestor1, ancestor2 = ancestor2, ancestor1
      node1, node2 = node2, node1
    # If ancestor lists not same lengths, make second list shorter
    diff = len(ancestor2) - len(ancestor1)
    while diff:
      node2 = node2.parent
      diff -= 1
    # Now that both same length, traverse in tandem until find match
    while node1 is not node2:
      node1 = node1.parent
      node2 = node2.parent
    return node1

  def inorder_no_space(self):
    """ Return inorder traversal using O(1) space """
    ret = []
    node = self.root
    prev = None
    while node:
      # Just came from parent, need to explore children
      if prev is node.parent:
        prev = node
        if node.left:
          node = node.left
        elif node.right:
          ret.append(node.value)
          node = node.right
        else:
          ret.append(node.value)
          node = node.parent
      # Just visited left child
      elif prev is node.left:
        prev = node
        ret.append(node.value)
        if node.right:
          node = node.right
        else:
          node = node.parent
      # Just visited right child
      else:
        prev = node
        node = node.parent
    return ret
