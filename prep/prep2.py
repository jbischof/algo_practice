"""
Final prep for showtime
"""
import heapq

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

