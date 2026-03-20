import random
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp


def generate_list(n=10):
    """Generate random list of n unique integers from 1 to 100"""
    return random.sample(range(1, 101), n)

def get_target(arr):
    """Pick a random target value from the list"""
    return random.choice(arr)

def generate_edge_list(num_vertices, max_edges_per_vertex=3, max_weight=10):
    """Generate a random UNDIRECTED connected weighted graph."""
    
    edges = set()

    # Ensure connectivity with a simple chain (spanning tree)
    for u in range(num_vertices - 1):
        v = u + 1
        w = random.randint(1, max_weight)
        edges.add((u, v, w))

    # Add extra random edges
    for u in range(num_vertices):
        num_edges = random.randint(0, max_edges_per_vertex)

        while True:
            current = sum(1 for (a, b, _) in edges if a == u or b == u)
            if current >= num_edges:
                break

            v = random.randint(0, num_vertices - 1)
            if v == u:
                continue

            w = random.randint(1, max_weight)

            a, b = sorted((u, v))
            edges.add((a, b, w))

    return list(edges)

def plot_graph(edges, highlight_edges=None, node_colors=None, title="Graph", layout_seed=42):
    """Visualise a graph from an edge list using networkx + matplotlib see alias"""
    G = nx.Graph()

    # Add edges with weights
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Compute layout once so all stages share the same geometry
    pos = nx.kamada_kawai_layout(G, weight="weight")

    # Default node colours
    if node_colors:
        colors = [node_colors.get(n, "lightblue") for n in G.nodes()]
    else:
        colors = "lightblue"

    # Draw base graph
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=800,
        font_size=12,
        edge_color="gray",
        width=2
    )

    # Draw edge weights
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight edges (e.g., MST, Dijkstra tree)
    if highlight_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=highlight_edges,
            width=4,
            edge_color="red"
        )

    plt.title(title)
    plt.show()

def extract_tree_edges(parent):
    edges = []
    for v, p in enumerate(parent):
        if p is not None:
            edges.append((p, v))
    return edges

def distance_to_colors(distance):
    return {node: distance[node] for node in range(len(distance))}

def edge_list_to_adj_list(edges):
    """Converts edge lists to an adjacent list"""
    # infer number of vertices from the edges
    max_node = 0
    for u, v, _ in edges:
        max_node = max(max_node, u, v)

    num_vertices = max_node + 1

    # build adjacency list
    graph = [[] for _ in range(num_vertices)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph