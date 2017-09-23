import binary_tree as bt
import collections

class BST(bt.BinaryTree):
  def check_valid(self):
    """Verifies binary tree has BST property using inorder traversal.
    If tree is BST, inorder should produce keys in sorted order.
    Time complexity: O(N) (each node traversed once)
    Space complexity: O(1)
    """

    # Empty tree trivially satisfies property
    if not self.root:
      return True
    return self.check_valid_helper(self.root, None)


  def check_valid_helper(self, node, prev):
    """Helper function for recursive validity check."""

    if node.left and not self.check_valid_helper(node.left, prev):
      return False
    if prev and node.value < prev.value:
      return False
    # Now this node is the most recent
    prev = node
    if node.right and not self.check_valid_helper(node.right, prev):
      return False
    return True


  def search_with_parent(self, value):
    """Search for value in BST, finding parent as well.

    Time Complexity: O(H), where H is height of tree
    Space Complexity: O(1)
    Args:
      value: value to find
    Returns:
      (Node, parent node) tuple or None if not found
    """

    if not self.root:
      return None
    return self._search_with_parent_helper(self.root, None, value)


  def _search_with_parent_helper(self, node, parent, value):
    if value == node.value:
      return (node, parent)
    if value < node.value:
      if not node.left:
        return None 
      return self._search_with_parent_helper(node.left, node, value)
    if value > node.value:
      if not node.right:
        return None 
      return self._search_with_parent_helper(node.right, node, value)


  def search(self, value):
    """Search for value in BST.

    Time Complexity: O(H), where H is height of tree
    Space Complexity: O(1)
    Args:
      value: Value to find
    Returns:
      Node if found for None if not 
    """

    ret = self.search_with_parent(value)
    if ret is None:
      return None
    return ret[0]


  def insert(self, node):
    """Insert new value into BST.

    Time complexity: O(log N) if balanced
    Space complexity: O(1)
    Args:
      node: node to add to tree
    """

    if not self.root:
      self.root = node
      return
    current = self.root
    while True:
      if node.value > current.value:
        if current.right:
          current = current.right
        else:
          current.right = node
          break
      else:
        if current.left:
          current = current.left
        else:
          current.left = node
          break


  def remove_value(self, value):
    """Remove first occurrence of value from BST.

    May need to remove recursively if node has two children.
    TODO(bischof): rewrite without using search function for cleaner approach 
    Time complexity: O(log N) if balanced
    Space complexity: O(log N)
    Args:
      value: Value to be removed from tree
    Returns:
      Removed node or None if value not found
    """

    # Find node in tree with parent
    res = self.search_with_parent(value)
    if not res:
      return None
    node, parent = res
    if node.left and node.right:
      # If two children, need to replace with next largest node
      # (smallest node in right subtree)
      # Find and remove next largest from tree recursively
      next_largest = self.next_largest(node.value)
      self.remove_value(next_largest.value)
      # Put next_largest into parent and child relations of removed node
      if parent and parent.left is node:
        parent.left = next_largest
      elif parent and parent.right is node:
        parent.right = next_largest
      else:
        # Otherwise dealing with root node
        self.root = next_largest
      next_largest.left = node.left
      next_largest.right = node.right
    elif node.left:
      # If only one child, hook directly to parent node
      if parent and parent.left is node:
        parent.left = node.left
      elif parent and parent.right is node:
        parent.right = node.left
      else:
        # Otherwise dealing with root node
        self.root = node.left
    elif node.right:
      # If only one child, hook directly to parent node
      if parent and parent.left is node:
        parent.left = node.right
      elif parent and parent.right is node:
        parent.right = node.right
      else:
        # Otherwise dealing with root node
        self.root = node.right
    else:
      # Node is childless, delete directly
      if parent and parent.left is node:
        parent.left = None
      elif parent and parent.right is node:
        parent.right = None
      else:
        # Otherwise dealing with root node
        self.root = None
    # Clear and return node
    node.left = node.right = None
    return node
    

  def next_largest(self, value):
    """Search for next largest value in BST.

    Time Complexity: O(H), where H is height of tree
    Space Complexity: O(1)
    Args:
      value: baseline value
    Returns:
      Node or None if 'value' larger than entire tree      
    """

    return self.next_largest_helper(self.root, value, None)


  def next_largest_helper(self, node, value, last_largest):
    """Search for value with binary search, keeping track of the last largest
    value seen (which will be the closest in value by definition) in case
    end search on empty left child (where won't remember last largest you saw).

    Args:
      node: current node in traversal
      value: baseline value
      last_largest: Smallest value >= baseline value seen so far
    Returns:
      Node or None if 'value' larger than entire tree      
    """

    if value < node.value:
      last_largest = node
      if not node.left:
        return last_largest 
      return self.next_largest_helper(node.left, value, last_largest)
    if value >= node.value:
      if not node.right:
        return last_largest
      return self.next_largest_helper(node.right, value, last_largest)


  def k_largest(self, k):
    """Return K largest values in BST by reverse inorder traversal.

    Time complexity: O(H + k)
    Space complexity: O(k)
    Args:
      k: Number values to return
    """

    ret = []
    self._k_largest_helper(self.root, k, ret)
    return ret
  

  def _k_largest_helper(self, node, k, ret):
    if node.right:
      self._k_largest_helper(node.right, k, ret)
    if len(ret) < k:
      ret.append(node.value)
    else:
      return
    if node.left:
      self._k_largest_helper(node.left, k, ret)


  def k_smallest(self, k):
    """Return K smallest values in BST by inorder traversal.

    Time complexity: O(H + k)
    Space complexity: O(k)
    """

    ret = []
    self._k_smallest_helper(self.root, k, ret)
    return ret
  

  def _k_smallest_helper(self, node, k, ret):
    if node.left:
      self._k_smallest_helper(node.left, k, ret)
    if len(ret) < k:
      ret.append(node.value)
    else:
      return
    if node.right:
      self._k_smallest_helper(node.right, k, ret)


class Webpage(object):
  def __init__(self, id):
    self.id = id


class WebpageIndex(object):
  def __init__(self):
    self.hashmap = collections.Counter() 
    self.bst = BST()


  def update(self, page):
    """Update page visit counts with Webpage log.

    Time complexity: O(log N) for BST pop and insert
    Space complexity: O(1)
    Args:
      page: Webpage object
    """

    if page.id not in self.hashmap:
      self.hashmap[page.id] = 1
      self.bst.insert(bt.Node((1, page.id)))
      return
    old_count = self.hashmap[page.id]
    self.hashmap[page.id] += 1
    node = self.bst.remove_value((old_count, page.id))
    # Update count and place in tree
    node.value = (node.value[0] + 1, node.value[1])
    self.bst.insert(node)


  def update_list(self, page_list):
    """Perform update on list of webpages.
    
    Time complexity: O(N * log(M + N)), where M current size of tree
    Args:
      page_list: list of Webpage objects
    """

    for page in page_list:
      self.update(page)


  def top_k_visited(self, k):
    """Returns list of ids for k most visited pages.
    
    Time complexity: O(H + k).
    """

    return [val[1] for val in self.bst.k_largest(k)]

