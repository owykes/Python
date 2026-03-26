from algorithms.utils.helper import generate_edge_list
from algorithms.utils.helper import edge_list_to_unweighted_adj_list

def dfs(graph, start):
    """
    Depth-First Search (DFS)

    Returns:
        order: list of nodes in visitation order
        parent: list representing DFS tree
    """
    n = len(graph)

    if not (0 <= start < n):
        raise ValueError("Start node is out of bounds")

    visited = [False] * n
    parent = [None] * n
    order = []

    stack = [start]

    while stack:
        u = stack.pop()

        if not visited[u]:
            visited[u] = True
            order.append(u)

            # Add neighbours in reverse order so DFS explores
            # them in the natural left-to-right order
            for v in reversed(graph[u]):
                if not visited[v]:
                    parent[v] = u
                    stack.append(v)

    return order, parent

if __name__ == "__main__":
    edges = generate_edge_list(6)
    graph = edge_list_to_unweighted_adj_list(edges)

    order, parent = dfs(graph, start=0)

    print("Order:", order)
    print("Parent:", parent)
