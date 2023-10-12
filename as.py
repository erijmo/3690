def a_star(start, goal, heuristic, connections):
    open_set, closed_set = [(start, [start])], set()

    while open_set:
        current, path = open_set.pop(0)

        if current == goal:
            return path

        closed_set.add(current)

        if current in connections:
            neighbors = [(n, path + [n]) for n in connections[current] if n not in closed_set]
            neighbors.sort(key=lambda x: heuristic.get(x[0], 0) + connections[current][x[0]])
            open_set.extend(neighbors)

    return None

heuristic = {
    'S': 10, 'A': 8, 'B': 9, 'C': 7, 'D': 4, 'E': 3, 'F': 0, 'G': 6, 'H': 6
}

connections = {
    'S': {'A': 3, 'B': 2, 'C': 5},
    'A': {'C': 3, 'G': 2},
    'B': {'A': 4, 'D': 6},
    'C': {'B': 4, 'H': 3},
    'D': {'E': 2, 'F': 3},
    'E': {'F': 5},
    'G': {'E': 5, 'D': 4},
    'H': {'A': 4, 'D': 4}
}

start, goal = 'S', 'F'

path = a_star(start, goal, heuristic, connections)
if path:
    print("Path:", path)
else:
    print("Goal not reachable.")
