"""Graph problems."""
from collections import deque, Counter
import heapq

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.edges = []
        self.distance = float('inf')
        self.visited = False
        self.from_node = None

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return (f"{self.value}: Distance: {self.distance}, " 
        f"Visited: {self.visited}, From Node: {self.from_node.value}")


class Edge(object):
    def __init__(self, value, node_to=None, node_from=None):
        self.value = value
        self.node_to = node_to
        self.node_from = node_from

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return (
        f"Weight: {self.value}, "
        f"From: {(self.node_from.value if self.node_from else None)}, "
        f"To: {(self.node_to.value if self.node_to else None)}")


def find_maze_path(maze, start, end):
    """
    Find a valid path through maze, if one exists.

    Args:
        maze: A 2D array representing the maze. Open squares are one and closed
        squares are zero.
        start: Index of start position
        end: Index of end position
    Returns:
        path: A list of indicies traveled from start to end.

    Idea:
        Consider the maze to be a graph. Squares are connected if they are
        adjacent and both are open (`1`). Use a queue to record nodes to be
        visited. At each node add all connected neighbors to the queue.
        Time: O(|V| + |E|), Space: O(|E|)

        Hard part will be recreating the path. In the case maintain a "node 
        from" map that states the node from which traveled to each valid node.

    Baby example:
    [
    #    0  1  2  3  4
        [0, 0, 1, 1, 1], # 0
        [0, 1, 0, 1, 0], # 1
        [0, 1, 1, 1, 0], # 2
        [1, 1, 0, 1, 0], # 3
    ]
    start: (3, 0); end: (0, 4)
    node, queue 
    (3, 0), [(3, 1)]
    (3, 1), [(2, 1)]
    (2, 1), [(1, 1), (2, 2)]
    (1, 1), [(2, 2)]
    (2, 2), [(2, 3)]
    (2, 3), [(3, 3), (1, 3)]
    (3, 3), [(1, 3)]
    (1, 3), [(0, 3)]
    (0, 3), [(0, 2), (0, 4)]
    (0, 2), [(0, 4)]
    (0, 4), []
    return True
    """

    queue = deque([start])
    height = len(maze)
    width = len(maze[0])
    from_node = {}

    while queue:
        node = queue.popleft()
        if node == end:
            # Recover the path
            path = [node]
            while node != start:
                path.append(from_node[node])
                node = from_node[node]
            path.reverse()
            return True, path
        # Mark as visited
        maze[node[0]][node[1]] = 0
        if node[0] < height - 1 and maze[node[0] + 1][node[1]]:
            # Go down
            new_node = (node[0] + 1, node[1])
            queue.append(new_node)
            from_node[new_node] = node
        if node[0] > 0 and maze[node[0] - 1][node[1]]:
            # Go up
            new_node = (node[0] - 1, node[1])
            queue.append(new_node)
            from_node[new_node] = node
        if node[1] < width - 1 and maze[node[0]][node[1] + 1]:
            # Go right
            new_node = ((node[0], node[1] + 1))
            queue.append(new_node)
            from_node[new_node] = node
        if node[1] > 0 and maze[node[0]][node[1] - 1]:
            # Go left 
            new_node = ((node[0], node[1] - 1))
            queue.append(new_node)
            from_node[new_node] = node
    return False, None


def flood_fill(image, seed):
    """
    Flood color of opposite color of given node to all adjacent nodes of the
    same color. In place.

    Args:
        image: A binary 2D matrix where every row the same length.
        seed: A tuple of coordinates in the image.

    Returns:
        None.

    Idea: Do BFS from seed nodes and flip all reachable nodes

    Baby example:
    [
    #    0  1  2  3  4
        [0, 0, 1, 1, 1], # 0
        [0, 1, 0, 0, 0], # 1
        [0, 1, 1, 1, 0], # 2
        [1, 1, 0, 1, 0], # 3
    ]
    seed: (2, 1)
    color = 1
    node, flip?, queue 
    (2, 1), yes, [(3, 1), (1, 1), (2, 2), (2, 0)]
    (3, 1), yes, [(1, 1), (2, 2), (2, 0), (4, 1), (2, 1), (3, 2), (3, 0)]
    (1, 1), yes, [(2, 2), (2, 0), (4, 1), (2, 1), (3, 2), (3, 0), (2, 1), 
                  (0, 1), (1, 2), (1, 0)]
    (2, 2), yes, [(2, 0), (4, 1), (2, 1), (3, 2), (3, 0), (2, 1), (0, 1), 
                  (1, 2), (1, 0), (3, 2), (1, 2), (2, 3), (2, 1)]
    (2, 0), no,  [(4, 1), (2, 1), (3, 2), (3, 0), (2, 1), (0, 1), 
                  (1, 2), (1, 0), (3, 2), (1, 2), (2, 3), (2, 1)]
    (4, 1), no,  [(4, 1), (2, 1), (3, 2), (3, 0), (2, 1), (0, 1), 
                  (1, 2), (1, 0), (3, 2), (1, 2), (2, 3), (2, 1)]
    (2, 1), no,  [(2, 1), (3, 2), (3, 0), (2, 1), (0, 1), (1, 2), (1, 0), 
                  (3, 2), (1, 2), (2, 3), (2, 1)]
    (3, 2), no,  [(3, 2), (3, 0), (2, 1), (0, 1), (1, 2), (1, 0), 
                  (3, 2), (1, 2), (2, 3), (2, 1)]
    (3, 0), yes,  [(3, 0), (2, 1), (0, 1), (1, 2), (1, 0), (3, 2), (1, 2), 
                   (2, 3), (2, 1), (4, 0), (2, 0), (3, -1), (3, 1)]
    etc etc

    I like gating before enqueue personally. Definitely a lot less space and
    easier to debug.
    """

    queue = deque([seed])
    height = len(image)
    width = len(image[0])
    color = image[seed[0]][seed[1]]
    while queue:
        node = queue.popleft()
        # Make sure coordinates in image and the right color
        if not (
                node[0] < height and 
                node[0] >= 0 and 
                node[1] < width and 
                node[1] >= 0 and
                image[node[0]][node[1]] == color
        ):
            continue
        queue.append((node[0] + 1, node[1]))
        queue.append((node[0] - 1, node[1]))
        queue.append((node[0], node[1] + 1))
        queue.append((node[0], node[1] - 1))
        # Flip this node color
        image[node[0]][node[1]] = 1 - color


def has_cycle(graph):
    """
    Detect if directed graph has cycles.

    Idea: Cycle in graph if child node of DFS tree points back to parent.
    Maintain set of "grey" unprocessed nodes and if during traversal point back
    to grey node then cycle exists.

    Time: O(|V| + |E|), Space: O(|V|)
    graph = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['F'],
        'D': ['A'],
        'E': ['D'],
        'F': [],
    }

    # No cycles in this graph unless D->A edge is added
                 A
              ^     \
         (c) /       v 
             D       B -> C
             ^      /      \
              \    v        v
                E           F

    # This graph has no cycles but multiple nodes point to C
    # This is OK because C only points to childless node F
                 A------\
                    \    \
                     v    v 
             D       B -> C
             ^      /      \
              \    v        v
                E           F

    Start: B
    node, white, grey, ret
    -, [A, B, C, D, E, F], [], False
    B, [A, C, D, E, F], [B], False
    C, [A, D, E, F], [B, C], False
    F, [A, D, E], [B, C], False
    E, [A, D], [B, E], False
    D, [A], [B], False
    A, [], [], False
    return False

    Now add back edge D -> A, same until hit D
    D, [A], [B, D], False
    A, [], [B, D], False -> but A points to B so return True!

    Finally, add edge between A and C in first problem. Can see this doesn't
    make a difference since C is out of the grey set by the time you get to A.
    """

    white = set(graph.keys())
    grey = set()
    while white:
        if has_cycle_helper(white.pop(), graph, white, grey):
            return True
    return False


def has_cycle_helper(node, graph, white, grey):
    white.discard(node)
    grey.add(node)
    for edge in graph[node]:
        if edge in grey:
            # Back edge to parent!
            return True
        if has_cycle_helper(edge, graph, white, grey):
            return True
    grey.discard(node)
    return False
        

def topo_sort(g):
    """
    Return a topological sort of graph if possible.

    Args:
        g: Adjacency list
    Returns:
        Bool: Whether can be sorted (no cycles)
        List: The sort

    g = {
        'a': ['b', 'f'],
        'b': ['c', 'd', 'f'],
        'c': ['d'],
        'd': ['e', 'f'],
        'e': ['f'],
        'f': [],
    }

    node, grey, inlinks, ret
    -, [a], [a:0, b:1, c:1, d:2, e:1, f:4], []
    a, [b], [a:0, b:0, c:1, d:2, e:1, f:3], [a]
    b, [c], [a:0, b:0, c:0, d:1, e:1, f:2], [a, b]
    c, [d], [a:0, b:0, c:0, d:0, e:1, f:2], [a, b, c]
    d, [e], [a:0, b:0, c:0, d:0, e:0, f:1], [a, b, c, d]
    e, [f], [a:0, b:0, c:0, d:0, e:0, f:0], [a, b, c, d, e]
    f, [], [a:0, b:0, c:0, d:0, e:0, f:0], [a, b, c, d, e, f]
    return True, [a, b, c, d, e, f]

    Now suppose f points to b
    -, [a], [a:0, b:2, c:1, d:2, e:1, f:4], []
    a, [], [a:0, b:1, c:1, d:2, e:1, f:3], [a]
    Now the grey set is empty but still links!
    return False, []
    """

    inlinks = Counter({node: 0 for node in g})
    ret = []
    # Count in-links from each node
    for node in g:
        for edge in g[node]:
            inlinks[edge] += 1
    # Start traversal with parent-free nodes
    grey = set([node for node in inlinks if inlinks[node] == 0])
    while grey:
        node = grey.pop()
        ret.append(node)
        for edge in g[node]:
            inlinks[edge] -= 1
            if inlinks[edge] == 0:
                grey.add(edge)
    if any(inlinks[node] > 0 for node in inlinks):
        # If any links left they are backlinks and this is not a DAG
        return False, []
    return True, ret


def is_bipartite(g):
    """
    Detect if graph is bipartite and return halves if possible.

    Args:
        g: An adjacency list of graph
    Returns:
        Bool, node list

        1 ----- 4   
          \---\
        2 ----- 5
          \---\
        3 ----- 6

    g = {
        1: [4, 5, 6],
        2: [4, 6],
        3: [5, 6],
        4: [1, 2],
        5: [1, 3, 6 (bad)],
        6: [1, 2, 3, 5 (bad)],
    }

    Idea: Create two sets. Use BFS to travese graph. For every node put in one
    set and then put all connected nodes in another. When see edge to visited
    node, check that allocated to the wrong set.
    Time: O(|V| + |E|), Space: O(|E|)

    node, queue, sets, visited
    1: [4, 5, 6], [[1], [4, 5, 6]], [1, 4, 5, 6]
    4: [5, 6, 2], [[1, 2], [4, 5, 6]], [1, 4, 5, 6, 2]
    5: [6, 2, 3], [[1, 2, 3], [4, 5, 6]] -> but this fails set test since
                                            5 and 6 in same test


    # Try again with bad edge removed
    node, queue, sets, visited
    1: [4, 5, 6], [[1], [4, 5, 6]], [1, 4, 5, 6]
    4: [5, 6, 2], [[1, 2], [4, 5, 6]], [1, 4, 5, 6, 2]
    5: [6, 2, 3], [[1, 2, 3], [4, 5, 6]], [1, 4, 5, 6, 2, 3]
    6: [2, 3], [[1, 2, 3], [4, 5, 6]], [1, 4, 5, 6, 2, 3]
    2: [3], [[1, 2, 3], [4, 5, 6]], [1, 4, 5, 6, 2, 3]
    3: [], [[1, 2, 3], [4, 5, 6]], [1, 4, 5, 6, 2, 3]
    return True, [[1, 2, 3], [4, 5, 6]] 
    """

    sets = [set(), set()]
    visited = set()
    not_visited = set(g.keys())
    queue = deque()
    while queue or not_visited:
        if not queue:
            # Find disconnected parts of graph
            first = next(iter(not_visited)) 
            queue.append(first)
            visited.add(first)
            not_visited.remove(first)
            sets[0].add(first)
        node = queue.popleft()
        node_type = 0 if node in sets[0] else 1
        for edge in g[node]:
            if edge in sets[node_type]:
                # If edge in same set, partition impossible
                return False, []
            sets[1 - node_type].add(edge)
            if edge not in visited:
                queue.append(edge)
            visited.add(edge)
            not_visited.discard(edge)
    return True, sets


def dijkstra(start, end):
    """
    Implement dijkstra's algorithm

    Args:
        start: Starting node
        end: Destination node
    """

    heap = [start]
    start.distance = 0

    while heap:
        node = heapq.heappop(heap)
        if node.visited:
            # Possible to add node to queue multiple times since visited only
            # updated when node is black
            continue
        node.visited = True
        if node == end:
            path = path_from_endpoints(start, end)
            return end.distance, path
        for edge in node.edges:
            # Update distances
            new_node = edge.node_to
            if node.distance + edge.value < new_node.distance:
                new_node.distance = node.distance + edge.value
                # Remember where you came from
                new_node.from_node = node
            # Insert into priority queue if not visited
            if not new_node.visited:
                heapq.heappush(heap, new_node)

    # Destination not found
    return None, None


def path_from_endpoints(start, end):
    """
    Return traversal path from start to end node using `node_from` pointers.
    """

    path = [end.value]
    node = end
    while node != start:
        path.append(node.from_node.value)
        node = node.from_node
    path.reverse()
    return path


def mst(root):
    """
    Find the minimum spanning tree for graph g using Prim's algorithm.

    Args:
        root: Arbitrary node to use as starting point.
    Returns:
        int: Cost of MST
        dict: {Node.value: Edge}, Edge connecting each node to the MST

    Note: If graph not fully connected with find MST for subgraph containing the
    root.

    Time: O(E|log|V|), Space: O(log|E|)
    
    Example:
                  A                A
              4/  | 5\             | 
              B   |   E  -->   B   |   E
              |  3|   |2       |  3|   |2
             2|    \ /        2|    \ /
              C------D         C------D
                 1                1     
    node, heap, ret
    A, [(3, A, D), (4, A, B), (5, A, E)], {A: None}
    D, [(1, D, C), (2, D, E), (4, A, B), (5, A, E)]
       {A: None, D: (3, A, D)}
    C, [(2, D, E), (2, C, B), (4, A, B), (5, A, E)]
       {A: None, D: (3, A, D), C: (1, D, C)}
    E, [(2, C, B), (4, A, B), (5, A, E)]
       {A: None, D: (3, A, D), C: (1, D, C), E: (2, D, E)}
    B, [(4, A, B), (5, A, E)]
       {A: None, D: (3, A, D), C: (1, D, C), E: (2, D, E), B: (2, C, B)}

    return 8, {A: None, D: (3, A, D), C: (1, D, C), E: (2, D, E), B: (2, C, B)}
 
    """

    heap = [edge for edge in root.edges]
    heapq.heapify(heap)
    root.visited = True
    ret = {root.value: Edge(0, root)}

    while heap:
        # Pop the lowest cost edge not part of the tree
        edge = heapq.heappop(heap)
        node = edge.node_to
        if node.visited or node == edge.node_from:
            # No loops or visited nodes
            continue
        if node.value not in ret or edge.value < ret[node.value].value:
            ret[node.value] = edge

        # Process node's edges if not already explored
        for edge in node.edges:
            if not edge.node_to.visited:
                heapq.heappush(heap, edge)
        node.visited = True

    # Compute total cost
    cost = 0
    for edge in ret.values():
        cost += (edge.value if edge else 0)
    return cost, ret

