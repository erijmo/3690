def hill_climb(initial_state, goal_state, heuristic_values, connections):
    current_state = initial_state
    path = [current_state]

    while current_state != goal_state:
        neighbors = connections.get(current_state, {})

        if not neighbors:
            print("Stuck in a local minimum.")
            return path

        best_neighbor = min(neighbors, key=lambda neighbor: heuristic_values[neighbor])

        if heuristic_values[best_neighbor] < heuristic_values[current_state]:
            current_state = best_neighbor
            path.append(current_state)
        else:
            print("Stuck in a local minimum.")
            return path

    return path

heuristic_values = {
    'A': 7, 'B': 5, 'C': 3, 'U': 4, 'E': 2, 'G': 3, 'I': 6, 'J': 4, 'K': 1, 'Y': 2, 'M': 0
}

connections = {
    'A': {'B': 5, 'C': 3, 'U': 4},
    'B': {'E': 2, 'G': 3},
    'C': {'G': 3, 'I': 6, 'J': 4},
    'U': {'K': 1, 'Y': 2},
    'E': {'G': 3, 'M': 0},
    'G': {'M': 0},
    'I': {'M': 0},
    'J': {'K': 1},
    'K': {'J': 4},
    'Y': {'M': 0},
    'M': {}
}

initial_state = 'A'
goal_state = 'M'

path = hill_climb(initial_state, goal_state, heuristic_values, connections)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not reachable.")
