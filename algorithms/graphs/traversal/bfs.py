from collections import deque

def bfs(graph, start):
    """
    Performs Breadth-First Search on a graph.

    graph: dict where keys are nodes and values are lists of neighbours
    start: starting node
    """
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    