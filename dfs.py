def dfs(graph, root, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(root)
    
    for neighbor in graph[root]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited



if __name__ == '__main__':
    graph = {1:[8,5,2], 8:[6,4,3], 5:[], 2:[9], 6:[10,7], 4:[], 3:[], 9:[], 10:[], 7:[]}
    print(dfs(graph, 1))    