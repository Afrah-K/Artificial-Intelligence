def dls(graph, node, depth, limit, visited=None):
    if visited is None:
        visited = []
    visited.append(node)

    if depth == limit:
        return visited

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dls(graph, neighbor, depth + 1, limit, visited)
            if result:
                return result
    return None  # Return None if the limit is exceeded

if __name__ == '__main__':
    
    graph = {1:[8,5,2], 8:[6,4,3], 5:[], 2:[9], 6:[10,7], 4:[], 3:[], 9:[], 10:[], 7:[]}

    limit = 3  # Set the depth limit
    start_node = 1  # Set the starting node

    result = dls(graph, start_node, 0, limit)
    
    if result:
        print(f"DLS Sequence (Depth Limit {limit}):", result)
    else:
        print(f"DLS Sequence (Depth Limit {limit}): Depth limit exceeded.")
