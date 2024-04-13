import heapq

# Define a simple graph as an adjacency list
graph = {
    'S': [('A', 7), ('B', 2), ('C', 3)],'A': [('D', 4), ('B', 3)],'B': [('D', 4), ('H', 1)],
    'C': [('L', 2)],'D': [('F', 5)],'E': [],'F': [],'G': [('E', 2)],'H': [('F', 3), ('G', 2)],
    'I': [('K', 4)],'J': [('K', 4)],'K': [('E', 5)]
}

# Heuristic function (estimated cost from a node to the goal)
heuristic = {
    'A': 9,'B': 7,'C': 8,'D': 8,'E': 0,'F': 6,'G': 3,'H': 6,'I': 4,'J': 4,'K': 3,'S': 10
}

def astar_search(graph, start, goal):
    visited = set()
    priority_queue = [(heuristic[start], 0, start, [])]  # (f, g, node, path)

    while priority_queue:
        _, g, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path + [current_node]

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                f = g + cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (f, g + cost, neighbor, path + [current_node]))

    return []  # Return an empty path if the goal is not reachable

start_node = 'S'
goal_node = 'E'

path = astar_search(graph, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
    total_cost = sum(cost for current_node, next_node in zip(path, path[1:]) for neighbor, cost in graph[current_node] if neighbor == next_node)
    print(f"Total cost: {total_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
