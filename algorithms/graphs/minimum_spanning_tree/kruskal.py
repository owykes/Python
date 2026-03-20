# Kruskal - Minimum Spanning Tree - greedy alogrithm
# Connects all nodes in the same tree via minimum edge weight 
# Time Complexity: O(E * log E) or O(E * log V) 
from algorithms.utils.helper import generate_edge_list
from functools import cmp_to_key

def comparator(a,b):
    return a[2] - b[2];

def kruskals_mst(V, edges):

    # Sort all edges
    edges = sorted(edges,key=cmp_to_key(comparator))
    
    # Traverse edges in sorted order
    dsu = DSU(V)
    cost = 0
    count = 0
    mst_edges = []

    for x, y, w in edges:
        
        # Make sure that there is no cycle
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            mst_edges.append((x, y, w))
            count += 1
            
            if count == V - 1:
                break
    return cost, mst_edges
    
# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


if __name__ == '__main__':
    
    vertices = 6
    edges = generate_edge_list(vertices)
    print(f"Generated edges: {edges}")

    cost, mst = kruskals_mst(vertices, edges)
    print("MST cost:", cost)
    print("MST edges:", mst)

