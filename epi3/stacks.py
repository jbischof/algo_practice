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
