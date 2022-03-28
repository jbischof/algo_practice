from collections import deque

class Node():
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None


def is_tree_balanced(root):
    """
    Determine if difference in height of all left and right subtrees no
    greater than one.

    Idea: At each level of recusion send depth probes down both sides and
    check for the condition. Base condition is null node
    Time: O(N), Space: O(H)

              1
            /   \
           2     3
          / \
         4   5
              \
               6
    4: (1, True)
    6: (1, True)
    5: (2, True)
    2: (3, True)
    3: (1, True)
    1: (4, False)
    """

    # Base condition: null node
    if not root:
        return (0, True)

    left_height, is_left_bal = is_tree_balanced(root.left)
    right_height, is_right_bal = is_tree_balanced(root.right)

    is_bal = (
            abs(left_height - right_height) <= 1 and
            is_left_bal and is_right_bal
    )
    height = max(left_height, right_height) + 1
    return height, is_bal


def least_common_ancestor(root, node1, node2):
    """
    Find the greatest depth node that is an ancestor to node1 and node2 on a
    tree with root.

    Brute force: accumulate the ancestors of each node in a hash table. Then for
    the nodes of interest intersect their lists of ancestors and find the one 
    with the lowest depth. This requires calculating the depth of each node
    as well. Time: O(N), Space: O(N)

    Idea: For each node, determine if node1 and/or node2 was a descendant in a 
    postorder traversal of the tree. Then return the first node for which both
    are present.
    Time: O(N), Space: O(H)

    Root, node1, node2:
    1, 2, 3 -> 3
              1
            /   \
           2     3
          / \
         4   5
              \
               6
    1, 4, 6 -> 2
    4: (True, False, None)
    6: (False, True, None)
    5: (False, True, None)
    2: (True, True, 2)
    3: (False, False, None)
    1: (True, True, 2)
    """

    # Base condition: null node
    if root is None:
        return (False, False, None)

    node1_des_left, node2_des_left, lca_left = least_common_ancestor(
            root.left, node1, node2)
    node1_des_right, node2_des_right, lca_right = least_common_ancestor(
            root.right, node1, node2)
    node1_des = root is node1 or node1_des_left or node1_des_right
    node2_des = root is node2 or node2_des_left or node2_des_right

    # In determining lca status, give precedence to children so is "least"!
    lca_self = root if node1_des and node2_des else None
    lca = lca_left or lca_right or lca_self

    return (node1_des, node2_des, lca)
    

def sort_nodes_by_level(root):
    """
    Return a nested list of nodes in a binary tree. Each list should represent a
    level in the tree and be ordered left to right.

    Idea1: Send depth info up the tree in a DFS and write nodes of each depth to
    a hashmap of lists indexed by level. Time: O(N), Space: O(N)

    Idea2: Do a BFS of the tree and pass down depth info. That will have us
    explore the nodes in terms of height and make it easier to write them
    out to a nested array.

              1
            /   \
           2     3
          / \
         4   5
              \
               6
    Node, queue, level_array
    Null, [(1, 0)], []
    1, [(2, 1), (3, 1)], [[1]]
    2, [(3, 1), (4, 2), (5, 2)], [[1], [2]]
    3, [(4, 2), (5, 2)], [[1], [2, 3]]
    4, [(5, 2)], [[1], [2, 3], [4]]
    5, [(6, 3)], [[1], [2, 3], [4, 5]]
    6, [], [[1], [2, 3], [4, 5], [6]]
    """

    queue = deque([(root, 0)])
    level_array = []
    while queue:
        node, level = queue.popleft()
        if level + 1 > len(level_array):
            # Should never be more than one level ahead of list
            level_array.append([])
        level_array[level].append(node.value)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return level_array
        

def inorder_traversal_stack(root):
    """
    Inorder traversal with an explict stack (no recursion).
    Time: O(N), Space: O(N)
    However, there is a more optimal solution without a visited set.

              1
            /   \
           2     3
          / \
         4   5
              \
               6

    done, stack, ret 
    1: [], [1, 2], []
    2: [], [1, 2, 4], []
    4: [4], [1, 2], [4]
    2: [4, 2], [1, 5], [4, 2]
    5: [4, 2, 5], [1, 6], [4, 2, 5]
    6: [4, 2, 5, 6], [1], [4, 2, 5, 6]
    1: [4, 2, 5, 6, 1], [3], [4, 2, 5, 6, 1]
    3: [4, 2, 5, 6, 1, 3], [], [4, 2, 5, 6, 1, 3]
    """

    ret = []
    stack = [root]
    done = set()
    while stack:
        curr = stack.pop()
        if curr.left and curr.left not in done:
            stack.append(curr)
            stack.append(curr.left)
        else:
            # Process this node
            ret.append(curr.value)
            done.add(curr)
            if curr.right:
                stack.append(curr.right)
    return ret


def compute_successor(node, first=True):
    """
    Compute the next node in an inorder traversal given pointer to ref node.

              1
            /   \
           2     3
          / \
         4   5
              \
               6
    Example:
    1: return 3
    2: return 5
    3: Go to 1; return None
    4: return 2
    5: return 6
    6: Go to 5, go to 2, return 1
    return 1

    Idea: If node has right child, successor is leftmost node in that subtree.
    If no right child, need to use parent pointers to go back up the tree.
    - If no parent, you are the root! Return None
    - If you're the left child of your parent, parent is the answer
    - If you're the right child of your parent, algorithm essentially recurses
      up the tree, looking for the successor of your parent as if it had no
      right child.
    Time: O(H), Space: O(H)
    """

    # Base cases
    if node.right and first:
        # Right child: find leftmost node of subtree
        node = node.right
        while node.left:
            node = node.left
        return node
    elif not node.parent:
        # Root without right child
        return None
    elif node.parent.left == node:
        # Left child of parent without own right child
        return node.parent

    # Uh oh, you are the right child of your parent.
    # Recurse on the parent without right subtree
    return compute_successor(node.parent, False)


def compute_successor_nr(node):
    """
    Compute the next node in an inorder traversal given pointer to ref node.
    
    This version does not use the tail recursion of the previous one.

              1
            /   \
           2     3
          / \
         4   5
              \
               6
    Example:
    1: return 3
    2: return 5
    3: Go to 1; return None
    4: return 2
    5: return 6
    6: Go to 5, go to 2, return 1
    return 1

    Idea: If node has right child, successor is leftmost node in that subtree.
    If no right child, need to use parent pointers to go back up the tree.
    - If no parent, you are the root! Return None
    - If you're the left child of your parent, parent is the answer
    - If you're the right child of your parent, algorithm essentially recurses
      up the tree, looking for the successor of your parent as if it had no
      right child.
    Time: O(H), Space: O(H)
    """

    # Base cases
    if node.right:
        # Right child: find leftmost node of subtree
        node = node.right
        while node.left:
            node = node.left
        return node
    elif not node.parent:
        # Root without right child
        return None

    # If triggered, you are the right child of your parent.
    # Need to find subtree where your parent is left child
    while node.parent and node.parent.right == node:
        node = node.parent

    return node.parent

