def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    return _dijkstra(graph, start, end, distances)

def _dijkstra(graph, current, end, distances):
    if current == end:
        return distances
    for neighbor, weight in graph[current].items():
        if distances[neighbor] > distances[current] + weight:
            distances[neighbor] = distances[current] + weight
            _dijkstra(graph, neighbor, end, distances)
    return distances