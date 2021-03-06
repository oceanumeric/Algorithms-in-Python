"""
Shortest Path with Dijkstra's Algorithm
To keep track of the total cost from the start node to each destination we will
make use of a distances dicionary which we will initialize to 0 for the start
vertex, and infinity for the other vertices.
"""

import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        print(pq)
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance  # replace infity
                heapq.heappush(pq, (distance, neighbor))

    return distances


def main():

    example_graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }

    print(calculate_distances(example_graph, 'U'))


if __name__ == "__main__":
    main()
