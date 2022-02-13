"""Stack problems."""

class StackWithMax(object):
    """
    Implement stack with max API. That is, should be able to poll the current
    max at any time. 

    Brute force: Scan the list every poll. Time: O(N), Space: O(1)

    Idea: With every push, record the max so far. Then if there are further pops
    will always have access to the max for the truncated list. 
    """
    def __init__(self):
        self.stack = []

    def max(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

    def push(self, x):
        if not self.stack or x > self.max():
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.max()))

    def pop(self):
        return self.stack.pop()[0]


class PostingNode(object):
    def __init__(self): 
        self.order = None
        self.next = None
        self.jump = None


def traverse_posting_list(node, pos=-1):
    """Recursive function to traverse plist in jump-first order."""

    node.order = pos + 1
    if node.jump and not node.jump.order:
        traverse_posting_list(node.jump, node.order)
    if node.next and not node.next.order:
        traverse_posting_list(node.next, node.order)


def traverse_posting_list_iter(head):
    stack = [head]
    order = 0
    while stack:
        node = stack.pop()
        if not node.order:
            node.order = order
            order += 1
        if node.next and not node.next.order:
            stack.append(node.next)
        if node.jump and not node.jump.order:
            stack.append(node.jump)


class Building(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height


def sunset_view(a):
    """Determine which buildings have sunset view (west-facing).
    
    Args:
        a: List of Buildings in east-to-west order

    Returns:
        Buildings that have a sunset view
    
    East        ->      West
    [a, b, c, d, e, f, g, h, i]
    [6, 3, 9, 2, 6, 0, 8, 2, 1]
    Ans: i, h, g, c

    Idea: building has view if no other buildings west of it are higher.
    Therefore only makes sense to process array from the back so can keep
    track of highest building seen so far. Seems quite similar to the stack
    with max API problem.

    Time: O(N), Space: O(1)
    """

    max_so_far = -1
    views = []
    while a:
        curr = a.pop()
        if curr.height > max_so_far:
            views.append(curr)
            max_so_far = curr.height
    return views


def sunset_view_stream(stream):
    """
    Determine which buildings have a sunset view when only see one at a time
    in east to west order.

    Brute force: Every new building automatically gets a view, so add to view
    list. Then scan existing list to see if that building gets in the way of 
    any of the others. 
    Time: O(N^2), Space: O(M), where M number of buildings with a view.

    Idea: Similar to brute force, but with new entry pop elements of list until
    see a taller building, which by defintion would have a view. In this way
    each building only popped once so O(N) time and O(M) space.
    """

    views = []
    for b in stream:
        while views and views[-1].height < b.height:
            # Remove all shorter buildings
            views.pop()
        views.append(b)
    return views
        
