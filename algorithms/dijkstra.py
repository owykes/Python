import sys
import heapq
from helper import generate_graph

# Dijkstra's shortest path

def dijkstra(adjacent, source):

    vertices = len(adjacent)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    distance = [sys.maxsize] * vertices

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
                heapq.heappush(pq, (distance[v], v))

    # Return the final shortest distances from the source
    return distance

if __name__ == "__main__":
    graph = generate_graph(6)
    print("Generated graph:")
    print(graph)

    distances = dijkstra(graph, 0)
    print("\nShortest distances from node 0:")
    print(distances)
