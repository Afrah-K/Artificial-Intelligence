import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        print(str(vertex)+ " ", end = " ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
if __name__ == '__main__':
    graph = {1:[8,5,2], 8:[6,4,3], 5:[], 2:[9], 6:[10,7], 4:[], 3:[], 9:[], 10:[], 7:[]}
    bfs(graph, 1)
    
