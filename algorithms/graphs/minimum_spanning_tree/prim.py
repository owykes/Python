import heapq
from algorithms.utils.helper import edge_list_to_adj_list, generate_edge_list
# Prim - Another minimum spanning tree- Prim's algorithm - greedy algorithm
# Begin by choosing the edge with the smallest weight
# Succesively add the edge with the smallest weight that are incident to a vertex already in the tree that does not form a circuit
# Stop when n - 1 edges have been added.

def prims_mst(V, edges):
    """Compute the Minimum Spanning Tree using Prim's algorithm."""
    # Convert edge list → adjacency list 
    adj = edge_list_to_adj_list(edges)

    visited = [False] * V
    mst_edges = []
    cost = 0

    # Start from node 0
    start = 0
    visited[start] = True
    visited_count = 1

    # Min-heap of (weight, u, v)
    min_heap = []
    for v, w in adj[start]:
        heapq.heappush(min_heap, (w, start, v))

    # Build MST
    while min_heap and visited_count < V:
        w, u, v = heapq.heappop(min_heap)

        if visited[v]:
            continue

        # Accept this edge
        visited[v] = True
        visited_count += 1
        mst_edges.append((u, v, w))
        cost += w

        # Add all edges from v
        for nxt, weight in adj[v]:
            if not visited[nxt]:
                heapq.heappush(min_heap, (weight, v, nxt))

    return cost, mst_edges


if __name__ == '__main__':
    from algorithms.utils.helper import generate_edge_list

    vertices = 6
    edges = generate_edge_list(vertices)
    print("Edges:", edges)

    cost, mst = prims_mst(vertices, edges)
    print("MST cost:", cost)
    print("MST edges:", mst)





