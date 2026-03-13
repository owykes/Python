import sys
import heapq
from helper import generate_edge_list, edge_list_to_adj_list, plot_graph, extract_tree_edges, distance_to_colors 

# Dijkstra's shortest path - pathfinding algorithm

def dijkstra(adjacent, source):

    vertices = len(adjacent)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    distance = [sys.maxsize] * vertices
    parent = [None] * vertices 

    # Distance from source to itself is 0
    distance[source] = 0
    heapq.heappush(pq, (0, source))

    # Process the queue until all reachable vertices are finalized
    # u = current node, v = a neighbour of u, w = the weight of the edge (cost)
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > distance[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adjacent[u]:
            # If we found a shorter path to v through u, update it
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                heapq.heappush(pq, (distance[v], v))

    # Return the final shortest distances from the source
    return distance, parent

if __name__ == "__main__":
    edges = generate_edge_list(6)
    print(f"Generated edges: {edges}")
   
    graph = edge_list_to_adj_list(edges)
    print(f"Adjacent list: {graph}")

    distance, parent = dijkstra(graph, 0)
    print(f"Shortest distances from node 0: {distance}")
    print(f"Parent array (shortest-path tree): {parent}")

    # A. Raw graph
    plot_graph(edges, title="Raw Graph")

    # B. Distance heatmap
    node_colors = distance_to_colors(distance)
    plot_graph(edges, node_colors=node_colors, title="Dijkstra Distances")

    # C. Shortest-path tree
    tree_edges = extract_tree_edges(parent)
    plot_graph(edges, highlight_edges=tree_edges, title="Dijkstra Tree")