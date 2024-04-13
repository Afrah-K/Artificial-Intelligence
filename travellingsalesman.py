import heapq
import networkx as nx

def minimum_spanning_tree(graph, visited):
    mst = nx.Graph()
    for u in visited:
        for v, weight in graph[u]:
            if v in visited:
                mst.add_edge(u, v, weight=weight)
    mst = nx.minimum_spanning_tree(mst)
    return mst
def tsp_astar(graph, start):
    num_cities = len(graph)
    heap = [(0, [start], set([start]))]  
    while heap:
        (cost, path, visited) = heapq.heappop(heap)
        current_city = path[-1]
        
        if len(visited) == num_cities:
            path.append(start)  # Return to the starting city
            return path, cost      
        for neighbor in graph[current_city]:
            neighbor_city, weight = neighbor
            if neighbor_city not in visited:
                new_cost = cost + weight
                new_path = path + [neighbor_city]
                new_visited = visited.copy()
                new_visited.add(neighbor_city)
                mst = minimum_spanning_tree(graph, new_visited)
                heuristic = sum(mst[u][v]['weight'] for (u, v) in mst.edges)
                heapq.heappush(heap, (new_cost + heuristic, new_path, new_visited))

    return None, None
# Create a graph with distances between cities
graph = {
    1: [(2, 12), (3, 10), (7, 12)], 2: [(3, 8), (4, 12)],  3: [(7, 9), (5, 3), (4, 11)],  4: [(5, 11), (6, 10)], 5: [(7, 7), (6, 6)], 6: [(7, 9)],  7: []
}
start_city = 1
best_tour, best_distance = tsp_astar(graph, start_city)
print("Best Tour:", best_tour)
print("Total Distance:", best_distance)
