from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    dist = [-1] * n
    dist[0] = 0
    queue = deque([0])
    
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if dist[next_node] == -1:
                dist[next_node] = dist[now] + 1
                queue.append(next_node)
    
    max_dist = max(dist)
    return dist.count(max_dist)
