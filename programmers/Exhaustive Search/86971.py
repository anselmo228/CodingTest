from collections import deque

def solution(n, wires):
    
    def bfs(start, visited, graph):
        queue = deque([start])
        visited[start] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count
    
    min_len = n
    
    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n+1)]
        for v1, v2 in temp_wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = [False] * (n + 1)
        count = bfs(1, visited, graph)
        temp_len = abs((n-count) - count)
        min_len  = min(min_len, temp_len)
        
    
    return min_len