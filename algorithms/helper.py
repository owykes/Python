import random

def generate_list(n=10):
    """Generate random list of n unique integers from 1 to 100"""
    return random.sample(range(1, 101), n)

def get_target(arr):
    """Pick a random target value from the list"""
    return random.choice(arr)

def generate_graph(num_vertices, max_edges_per_vertex=3, max_weight=10):
    """Generates a weighted graph in adjacent list form."""
    graph = []

    for u in range(num_vertices):
        neighbours = set() # set to prevent duplicates
        num_edges = random.randint(0, max_edges_per_vertex)

        while len(neighbours) < num_edges:
            v = random.randint(0, num_vertices - 1)
            if v == u: 
                continue 
            
            w = random.randint(1, max_weight)
            neighbours.add((v, w))

        graph.append(list(neighbours))

    return graph