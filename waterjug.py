from collections import deque

# Function to represent the state of water in jugs
class State:
    def __init__(self, x, y):
        self.x = x  # Water in Jug X
        self.y = y  # Water in Jug Y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"
# Function to perform BFS for the Water Jug Problem
def water_jug_bfs(capacity_x, capacity_y, target):
    visited = set()
    initial_state = State(0, 0)
    queue = deque([initial_state])
    while queue:
        current_state = queue.popleft()
        visited.add(current_state)

        # Check if the target state is reached
        if current_state.x == target or current_state.y == target:
            return current_state
        # Fill Jug X
        fill_x = State(capacity_x, current_state.y)
        if fill_x not in visited:
            queue.append(fill_x)
            visited.add(fill_x)
        # Fill Jug Y
        fill_y = State(current_state.x, capacity_y)
        if fill_y not in visited:
            queue.append(fill_y)
            visited.add(fill_y)
        # Empty Jug X
        empty_x = State(0, current_state.y)
        if empty_x not in visited:
            queue.append(empty_x)
            visited.add(empty_x)
        # Empty Jug Y
        empty_y = State(current_state.x, 0)
        if empty_y not in visited:
            queue.append(empty_y)
            visited.add(empty_y)
        # Pour water from X to Y
        pour_x_to_y = State(max(0, current_state.x - (capacity_y - current_state.y)), min(current_state.y + current_state.x, capacity_y))
        if pour_x_to_y not in visited:
            queue.append(pour_x_to_y)
            visited.add(pour_x_to_y)
        # Pour water from Y to X
        pour_y_to_x = State(min(current_state.x + current_state.y, capacity_x), max(0, current_state.y - (capacity_x - current_state.x)))
        if pour_y_to_x not in visited:
            queue.append(pour_y_to_x)
            visited.add(pour_y_to_x)
    return None

# Example usage:
jug_x_capacity = 4
jug_y_capacity = 3
target_amount = 2

result = water_jug_bfs(jug_x_capacity, jug_y_capacity, target_amount)
if result:
    print(f"Optimal solution found: {result}")
else:
    print("No solution found.")
