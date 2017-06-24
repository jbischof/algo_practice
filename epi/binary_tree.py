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
