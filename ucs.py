import heapq

def ucs(graph, start):
    visited = set()
    priority_queue = [(0, start)]  # Priority queue of tuples (cost, node)
    result = []

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor))
    return result

if __name__ == '__main__':
    # Define the graph with edge costs as a list of tuples
    graph = {1: [(8, 3), (5, 1), (2, 2)],8: [(6, 2), (4, 2), (3, 1)],5: [],2: [(9, 4)],6: [(10, 2), (7, 3)], 4: [], 3: [], 9: [], 10: [], 7: []}
    
    start_node = 1  # Set the starting node
    result = ucs(graph, start_node)
    print("UCS Sequence:", result)
