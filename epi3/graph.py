"""Graph problems."""
from collections import deque

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

    Idea: Need visited fields (or map) for graphs precisely because cycles are
    possible. If there is more than one way to get to a node we can go around
    in circles forever. However, with DAGs/trees this isn't possible so no
    visited map is needed.

    Therefore, do normal DFS on graph with visited map. If try to add a visited
    node back to the stack, return False. If stack empties without this event,
    return True.

    Time: O(|V| + |E|), Space: O(|V|)
    graph = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['F'],
        'D': ['A'],
        'E': ['D'],
        'F': [],
    }
                 A
              ^     \
             /       v 
             D       B -> C
             ^      /      \
              \    v        v
                E           F
    Start: A
    curr, stack, visited
    -, [A], []
    A, [B], [A]
    B, [C, E], [A, B]  
    E, [C, D], [A, B, E]
    D, [C, A] -> wait A in visited -> Return True
    If no connection between D and A:
    D, [C], [A, B, E, D]
    C, [F], [A, B, E, D, C]
    F, [], [A, B, E, D, C, F] -> Return False
    """

    stack = [next(iter(graph))]
    visited = set()
    while stack:
        node = stack.pop()
        for edge in graph[node]:
            if edge in visited:
                return True
            stack.append(edge)
            visited.add(edge)
    return False
