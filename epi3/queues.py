"""Queue problems."""

from collections import deque

class QueueWithMax(object):
    """Queue class with fast access to max.

    Brute force: Scan the collection every time max() method is called.
    Time: O(N), Space: O(1)

    q = [4, 8, 5, 2, 7, 2, 1, 4]
    This queue has max of 8. However, once first two elements popped, max will
    revert to 7. Alternatively, higher value could be added to right.

    Idea: Maintain a parallel BST with all the data in the deque. Then when
    values are pushed or popped they can also be removed from the BST. In this
    case max operation reduces to log(N) time, but push and pop are increased
    to log(N) time.

    Idea: Element with a greater value to the right can never be returned as the
    max. Therefore could maintain a parallel queue of max values that could be 
    pushed and popped as well. For example, in the existing queue only [8, 7, 4]
    could ever be the max. If 8 were popped, then this also could be popped 
    from max queue to yield 7. If 11 were added to the queue, all elements could
    be removed and 11 added. Note that this list must always be decreasing.

    Note: I am using a list implementation for simplicity, but this does incur
    O(N) pops.

    Max operation:
    Time: O(1), Space: O(N)
    """

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def push(self, x):
        self.queue.append(x)
        while self.max_queue:
            if self.max_queue[-1] < x:
                self.max_queue.pop()
        self.max_queue.append(x)

    def extend(self, x):
        for k in x:
            self.push(k)

    def pop(self):
        if self.queue[0] == self.max_queue[0]:
            self.max_queue.pop(0)
        return self.queue.pop(0)

    def max(self):
        return self.max_queue[0]

