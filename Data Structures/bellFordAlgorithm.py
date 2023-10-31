import sys

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

def bellman_ford(graph, src):

    # Step 1: Initialize distances from source to all other vertices
    dist = [float("Inf")] * graph.V
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(graph.V - 1):
        for s, d, w in graph.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    # Step 3: Check for negative-weight cycles
    for s, d, w in graph.graph:
        if dist[s] != float("Inf") and dist[s] + w < dist[d]:
            print("Graph contains negative weight cycle")          
            return