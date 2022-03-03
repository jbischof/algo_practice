"""Recursive problems."""
import random

def gen_permutations(a):
    """
    Generate all permutations of the elements in list.

    Args:
        a: A list
    Returns:
        A set of all permutations.

    Idea: A permutation can be defined recursively in terms of positions.
    If the first i positions are already chosen than the i+1 should be a
    random selection of the remaining ones

    Time: O(n * n!) because n! permutations and each perm requires n swaps.
    Space: O(1)
    """

    ret = []
    gen_permutations_helper(0, a, ret)
    return ret


def gen_permutations_helper(pos, a, ret):
    # Base case: all positions filled
    if pos == len(a) - 1:
        ret.append(a[:])
        return

    # Otherwise choose all remaining element for pos  
    for i in range(pos, len(a)):
        a[pos], a[i] = a[i], a[pos]
        gen_permutations_helper(pos + 1, a, ret)
        a[i], a[pos] = a[pos], a[i]


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_diameter(root):
    """
    Determine the longest path on a tree, where a path is defined as
    the number of edges between two leaf nodes.

    Idea: The longest path may or may not include the root. For example, the
    left child of the root might have a path of length 8 on its right and 7 on
    its left, but the root node has to choose one of these, not the sum.

    That suggests that each node must pass up *both* the longest path on the
    subtree as well as the longest *composable* branch that can be used by its
    parent; in this case 8. Note that 8 includes the subtree root itself.

    The solution at the parent is then the max of the paths on the left and
    right vs the sum of composable branches on left and right + 1.

    The base case is a None node, which returns (0, 0).
    
    Example:
    Longest path is between G and J (length 8)

    Example*: Longest path is between N and P and does not include the root
                      A
                   /     \
                  /       \
                 B         C
               /   \      / \
              D     E    H   I
             /      /          \
            K*     F            J
           /        \
         L*          G
        /             \
       M*              O*
      /                 \
     N*                  P*
    node lb, ld, rb, rd, mb, rd, bd
    N,   0,  0,  0,  0,  1,  1,  1
    N,   0,  0,  0,  0,  1,  1,  1
    G,   0,  0,  0,  0,  1,  1,  1
    F,   0,  0,  1,  1,  2,  2,  2
    E,   2,  2,  0,  0,  3,  3,  3
    B,   1,  1,  3,  3,  4,  5,  5
    """

    if root is None:
        return (0, 0)

    left_branch, left_dia = tree_diameter(root.left)
    right_branch, right_dia = tree_diameter(root.right)
    # Biggest branch reusable by parent node
    max_branch = max(left_branch, right_branch) + 1
    # Diameter of subtree rooted on this node
    root_dia = left_branch + right_branch + 1
    # Best diameter seem so far
    best_dia = max(root_dia, max(left_dia, right_dia))
    return max_branch, best_dia
