from collections import deque
from algorithms.utils.helper import edge_list_to_unweighted_adj_list
from algorithms.utils.helper import generate_edge_list

def bfs(graph, start):
    """
    Breadth-First Search (BFS)

    Returns:
        order: list of nodes in visitation order
        distance: list of shortest distances from start
        parent: list representing BFS tree
    """
    n = len(graph)

    if start < 0 or start >= n:
        raise ValueError("Start node is out of bounds")

    visited = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n

    queue = deque()

    visited[start] = True
    distance[start] = 0
    queue.append(start)

    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)

    return order, distance, parent

if __name__ == "__main__":
    
    edges = generate_edge_list(6)
    graph = edge_list_to_unweighted_adj_list(edges)
    order, distance, parent = bfs(graph, start=0)

    print("Order:", order)
    print("Distance", distance)
    print("Parent:", parent)
    
