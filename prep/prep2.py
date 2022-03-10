"""
Final prep for showtime
"""
import heapq
import collections

class Node(object):
    def __init__(self, value=None):
        self.value = value

def eval_tree_expr(root):
    """
    Task: evaluate arithmetic expression on tree
    

    Base case: raw number; yield value
    Operator: perform operation of left and right children

             '*'
            /   \
           '+'   3    
           / \
          2   4
    return 18

    2: return 2
    4: return 4 
    '+': return 2 + 4 = 6
    3: Return 3
    '*': Return 6 * 3 = 18
    """

    ops = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
    }

    if not isinstance(root.value, str):
        return root.value

    op = ops[root.value]
    return op(
            eval_tree_expr(root.right), 
            eval_tree_expr(root.left)
    )


class Annotation(object):
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end


class Event(object):
    def __init__(self, name, time, isEnd):
        self.name = name
        self.time = time
        self.isEnd = isEnd


def interval_annotation(a):
    """
    Input: a text being annotated, and list of intervals with annotation.

     012345678
    "some text"
    
    {
      [0, 4) -> X,
      [5, 8) -> Y,
      [3, 6) -> Z,
    }
    
    Output: a sequential list of text chunks with its annotations.
    
    {
      [0, 3) -> [X]     # "som"
      [3, 4) -> [X, Z]  # "e"
      [4, 5) -> [Z]     # " "
      [5, 6) -> [Y, Z]  # "t"
      [6, 8) -> [Y]     # "ex"
    }

    Brute force: maintain a list with element i pertaining to ith position in
    the input string. Seed every position with a empty nested list. Then iterate
    through every annotation and add its name to each relevant position.
    e.g., 
    [
        [X],     # 0  
        [X],     # 1,
        [X, Z],  # 3
        [Z],     # 4
        [Y, Z],  # 5
        [Y],     # 6
        [Y],     # 7
        [],      # 8
    ]
    Then iterate through the list and output ranges for each unique combination.
    Time: O(Nk), Space: O(Nk), where N length of string, k number of annotations

    This is fine, but ideally would merge the intervals themselves to get
    something closer to O(k) time and space.

    Idea: Sort the annotations by starting position. Then maintain a heap of
    active annotations keyed on end time while processing each new one. Every
    time see a new annotation check if any of the active ones are finished and
    add them to the output. Then add the new one to the heap. Clean up on the
    last one.
    Time: O(klogk), Space: O(k)

     012345678
    "some text"
    
    {
      [0, 4) -> X,
      [3, 6) -> Z,
      [5, 8) -> Y,
    }
    interval, curr, heap, res
    -, -, [], []
    X, 0, [(4, X)], []
    Z, 4, [(6, Z)], ('X': [0, 3), 'X,Z': [3, 4)] 
    Y, 4, [(8, Y)], ('X': [0, 3), 'X,Z': [3, 4), 'Z,Y': [5, 6)] 
    cleanup: ('X': [0, 3), 'X,Z': [3, 4), 'Z,Y': [5, 6), 'Y': [6, 8)] 

    Issue: In worst case could start with a complete annotation of the text and
    then have to handle all the other events with funky control flow rather
    than using the heap. Not a great solution.

    Idea2: Break up the annotations into an eventstream of start and stop
    positions. Then at each event either start or record a new annotation
    combination. Time: O(klogk), Space: O(k)
    [
        (0, s, X),
        (3, s, Z), 
        (4, e, X), 
        (5, s, Y), 
        (6, e, Z), 
        (8, e, Y), 
    ]
    event, curr, res
    -, -, []
    (0, s, X), (X, 0), []
    (3, s, Z), (XZ, 3), [(X, 0, 3)]
    (4, e, X), (Z, 4),  [(X, 0, 3), (XZ, 3, 4)]
    (5, s, Y), (ZY, 5), [(X, 0, 3), (XZ, 3, 4), (Z, 4, 5)]
    (6, e, Z), (Y, 6), [(X, 0, 3), (XZ, 3, 4), (Z, 4, 5), (ZY, 5, 6)]
    (8, e, Y), -, [(X, 0, 3), (XZ, 3, 4), (Z, 4, 5), (ZY, 5, 6), (Y, 6, 8)]
    """

    # Make event stream
    events = []
    for annot in a:
        events.append(Event(annot.name, annot.start, False))
        events.append(Event(annot.name, annot.end, True))
    events.sort(key=lambda x: x.time)

    res = []
    curr_set = set()
    curr_start = None
     
    for event in events:
        # Finish up any open events
        if curr_start is not None:
            res.append(
                    [
                        ''.join(sorted([item for item in curr_set])),
                        curr_start, 
                        event.time
                    ]
            )
        if event.isEnd:
            # Event ending
            curr_set.remove(event.name)
        else:
            # Event starting
            curr_set.add(event.name) 
        # Update current start position
        if len(curr_set) < 1:
            curr_start = None
        else:
            curr_start = event.time

    return res


def max_annot_overlap(a):
    """
    Determine max overlap of annotations on a string.

    Idea: split annotations into event stream and sort. Maintaining a counter,
    augment every time an event starts and and decrement every time it ends.
    Record max overlap seen so far.
    Time: O(NlogN), Space: O(N)

    Example:
    {
      [4, 6) -> W,
      [0, 4) -> X,
      [3, 6) -> Z,
      [5, 8) -> Y,
    }
     012345678
    X---
    W    --  
    Y     ---
    Z   ---
    Ans: 3

    Events:
    [
        (0, s, X),
        (3, s, Z), 
        (4, e, X), 
        (4, s, W), 
        (5, s, Y), 
        (6, e, Z), 
        (6, e, W), 
        (8, e, Y), 
    ]
    event, count, max_count
    -, 0, 0
    (0, s, X), 1, 1 
    (3, s, Z), 2, 2 
    (4, e, X), 1, 2 
    (4, s, W), 2, 2
    (5, s, Y), 3, 3
    (6, e, Z), 2, 3 
    (6, e, W), 1, 3
    (8, e, Y), 0, 3 
    return 3

    """

    # Split annotations into event stream
    events = []
    for annot in a:
        events.append(Event(annot.name, annot.start, False))
        events.append(Event(annot.name, annot.end, True))
    # Sort ensuring that ends come before starts with same time
    events.sort(key=lambda e: (e.time, e.isEnd))
     
    count, max_count = 0, 0
    for event in events:
        if event.isEnd:
            count -= 1
        else:
            count += 1
            max_count = max(count, max_count)
     
    return max_count


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.isDelete = False


def tree_eraser(root):
    """
    Given a binary tree, where each node has a "left" and "right" pointers, and 
    a predicate shouldBeErased(Node n), output the forest (collection of trees) 
    created by erasing the nodes indicated by shouldBeErased().

    Args:
        root: A node
    Retruns:
        A set of forest roots

    Example:
         F
        / \
       /   \
     [B]    G
     / \     \
    A   D    [I]
       / \   /
      C   E H
    
    
    In this example shouldBeErased() returns true for nodes B & I and false for 
    the other nodes, the resulting forest is : [ A, D, F, H ]
    
    A  F      D    H
        \    / \
         G  C   E

    Thoughts: need to clean up pointers and handle recursion given the deletion.
    Might also need to pass a reference to the ret object with the traversal so
    can append the new roots as needed. 

    Should handle deletion from the parent frame or the child frame? Unless
    parent pointers we are going to need to handle this from the parent frame.

    If have parent pointers, this might actually be easier from child frame. 
    Otherwise might have to go running after an arbitrary number of deleted
    children.

    Idea: Inorder traversal should work well here. When find a child node marked
    for removal can clean up pointers and start again. 

    Test:
         F
        / \
       /   \
     [B]    G
     / \     \
    A   D    [I]
       / \   /
      C   E H
    """

    ret = set()
    tree_eraser_helper(root, ret)
    return ret
    

def tree_eraser_helper(root, ret):
    # Base case: empty Node
    if root is None:
        return
     
    if root.parent is None and not root.isDelete:
        # Add any orphan nodes to output
        ret.add(root)
    if root.isDelete:
        # Clean up parent pointer
        if root.parent and root.parent.left == root:
            root.parent.left = None
        elif root.parent:
            root.parent.right = None
        # Clean up child parent pointers
        if root.left:
            root.left.parent = None
        if root.right:
            root.right.parent = None

    # Recurse to children
    tree_eraser_helper(root.left, ret)
    tree_eraser_helper(root.right, ret)
    return


class AlphaBlock(object):
    """
    A representation of a six-sided block with one char per face.

    The letters on the faces are not necessarily unique.
    """
    
    def __init__(self, chars):
        self.chars = chars
        self.char_count = collections.Counter(chars)
        self.upface = chars[0]


def spell_message(msg, blocks):
    """
    Reorder array of alpha blocks to spell the requested message.

    Brute force: Generate all permutations of the blocks and see if any can
    produce the desired message. Can prune any unpromising perms, but doesn't
    affect the worst case.
    Time: O(N * N!), Space: O(N)

    Idea: If char only present in one block, know where to put it. Otherwise
    ambiguity if a block has two chars of interest or if a char of interest is
    in multiple positions in the message.

    Greedy approach: For each position, look for the required letter among the
    blocks and fill it. If a letter is not available in the remaining blocks,
    search the previous blocks and swap it out. If have swapped out all previous
    positions and cannot move forward, return False.
    Actually this doesn't work because may need to swap the same position many
    times if some chars are easy to get but others are rare. Seems like we need
    the raw recursion.

    blocks = [
            AlphaBlock('UOIDLY'), # 0
            AlphaBlock('POCEIU'), # 1
            AlphaBlock('QWETJJ'), # 2
            AlphaBlock('AFRYGL'), # 3
            AlphaBlock('SLAQCE'), # 4
            AlphaBlock('DFSMGH'), # 5
    ]
    pos, i, blocks
             0  1  2  3  4  5
    0,   0, [0, 1, 2, 3, 4, 5]
    0,   1, [1, 0, 2, 3, 4, 5]
    0,   2, [2, 0, 1, 3, 4, 5]
    0,   3, [3, 0, 1, 2, 4, 5]
    1,   1, [3, 0, 1, 2, 4, 5]
    1,   2, [3, 1, 0, 2, 4, 5]
    2,   2, [3, 1, 0, 2, 4, 5]
    3,   3, [3, 1, 0, 2, 4, 5]
    4,   4, [3, 1, 0, 2, 4, 5]
    5,   5, [3, 1, 0, 2, 4, 5]
    """ 

    return spell_message_helper(0, msg, blocks)


def spell_message_helper(pos, msg, blocks):
    """
    Checks if possible to construct next char of message from next block.
    """

    # Base case: at the end. With backtracking this means we are successful!
    if pos == len(msg):
        return True

    # Try to construct char
    res = False
    for i in range(pos, len(msg)):
        blocks[pos], blocks[i] = blocks[i], blocks[pos]
        # Do not proceed if cannot construct msg with this block
        if msg[pos] in blocks[pos].char_count:
            blocks[pos].upface = msg[pos]
            res = spell_message_helper(pos + 1, msg, blocks)
        if res:
            break
        # Don't need this because if you fail all positions >= i are not
        # in an interesting order yet.
        # blocks[pos], blocks[i] = blocks[i], blocks[pos]
    return res


def remove_Xx_repeats(s):
    """
    Given a string that contains alphabetic characters, remove pairs of xX or Xx
    where the two chars in the pair are the same letter in different case. So 
    xX is removed, Xx is removed, but xx and XX are not. 

    Sample input: abcCkDdppGGa 
    Sample output: abkppGGa 

    Idea: Compare current char with next char to see if it is a "xX" type. If
    it is, do not write to new string.
    Time: O(N), Space: O(N)

              11
    012345678901
    abcCkDdppGGa

    i, ret
    0, 'a'
    1, 'ab'
    2, 'ab'
    4, 'abk'
    5, 'abk'
    7, 'abkp'
    8, 'abkpp'
    9, 'abkppG'
    10,'abkppGGa'
    """

    ret = []
    i = 0
    while i < len(s) - 1:
        if (
                (
                    (s[i].isupper() and s[i + 1].islower()) or
                    (s[i].islower() and s[i + 1].isupper())
                ) and
                s[i].lower() == s[i + 1].lower()
           ):
            i += 2
            continue
        ret.append(s[i])
        if i == len(s) - 2:
            # Handle last char if not paired with previous
            ret.append(s[i + 1])
        i += 1

    return ''.join(ret)
