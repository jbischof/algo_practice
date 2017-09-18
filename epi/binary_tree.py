class Node():
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None


class BinaryTree():
  def __init__(self, root=None):
    self.root = root


  def __eq__(self, other):
    """Equality means identical preorder and inorder traversals."""

    return (self.inorder() == other.inorder() and 
        self.preorder() == other.preorder())


  def __neq__(self, other):
    return not self.__eq__(other)


  @classmethod
  def from_preorder_inorder(cls, preorder, inorder):
    """Construct a tree from its preorder and inorder traversals. 
    Args:
      preorder: A list of node values in preorder
      inorder: A list of node values in inorder
    Returns:
      A BinaryTree class
    """

    tree = cls()
    tree.root = BinaryTree.from_preorder_inorder_helper(preorder, inorder)
    return tree


  @staticmethod
  def from_preorder_inorder_helper(preorder, inorder):
    """Performs recursion for preorder/inorder constructor."""

    # Base case: two levels of tree. This happens with <3 nodes or 3 nodes where
    # the second level is full.
    if len(preorder) < 3 or (len(preorder) == 3 and inorder[1] == preorder[0]):
      return BinaryTree.preorder_inorder_base_case(preorder, inorder)
    # Otherwise compare root location in preorder and inorder to divide up tree
    root = Node(preorder[0])
    # root_loc is location of root in inorder but also size of left tree
    root_loc = inorder.index(preorder[0]) 
    # Left tree nodes are in positions 1 to root_loc
    root.left = BinaryTree.from_preorder_inorder_helper(
        preorder[1:(1 + root_loc)], inorder[:root_loc])
    # Right tree nodes are in positions (root_loc + 1) to end
    root.right = BinaryTree.from_preorder_inorder_helper(
        preorder[(1 + root_loc):], inorder[(root_loc + 1):])
    return root


  @staticmethod
  def preorder_inorder_base_case(preorder, inorder):
    """Base case for preorder/inorder reconstruction: 3 or fewer nodes."""

    if not preorder:
      return None
    nomatch = preorder != inorder
    root = Node(preorder.pop(0))
    # If traversals don't match, need to extract left node 
    if nomatch:
      root.left = Node(preorder.pop(0))
    # Anything left is right node
    if preorder:
      root.right = Node(preorder.pop(0))
    return root 


  def preorder(self):
    """Returns pre-order traversal of tree."""

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
    """Returns in-order traversal of tree.
    
    Time complexity: O(N)
    Space complexity: O(H), where H is height of tree.
    """

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


  def inorder_no_recursion(self):
    """Returns in-order traversal without using recursion.

    Time complexity: O(N)
    Space complexity: O(H), where H is height of tree.
    """

    ret = []
    stack = []
    curr = self.root
    
    while stack or curr:
      if curr:
        # Going left
        stack.append(curr)
        curr = curr.left
      else:
        # Going up
        curr = stack.pop()
        ret.append(curr.value)
        # Going right
        curr = curr.right

    return ret


  def postorder(self):
    """Returns post-order traversal of tree."""

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
    """Return list of lists of nodes in tree.
    
    Each list contains items from one level in left-to-right order.
    """

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
    """Checks if all subtrees do not differ more than one level in height."""

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
    """Checks if left and right subtrees are mirror images."""

    if not self.root:
      return True
    return self.is_symmetric_helper(self.root.left, self.root.right)


  def is_symmetric_helper(self, left_node, right_node):
    """Compares left and right subtrees for equality recursively."""

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
    """Return list of ancestors of node.
    
    Only works if parent field is populated.
    """

    # TODO(bischof): just need to return depth to avoid O(N) storage
    res = []
    while node.parent:
      res.append(node.parent)
      node = node.parent
    return res


  def least_common_ancestor(self, node1, node2):
    """Find the least common ancestor of two nodes.
    
    Only works if parent field is populated. 
    """

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
    """Return inorder traversal using O(1) space."""

    ret = []
    node = self.root
    prev = None
    while node:
      # Just came from parent, need to explore children
      if prev is node.parent:
        prev = node
        if node.left:
          node = node.left
          continue
        ret.append(node.value)
        node = node.right or node.parent
      # Just visited left child, look right
      elif prev is node.left:
        prev = node
        ret.append(node.value)
        node = node.right or node.parent
      # Just visited right child
      else:
        prev = node
        node = node.parent
    return ret
