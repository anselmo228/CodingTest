from collections import deque

N, M = map(int, input().split())
graph = {}

for _ in range(M):
    i, j = map(int, input().split())
    if j not in graph:
        graph[j] = []
    graph[j].append(i)
    
result = []
answer = []

def bfs(start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        now = queue.popleft()

        if now in graph:
            for next in graph[now]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)
                    count += 1
    return count

max_count = 0

for i in range(N):
    result.append(bfs(i+1))
    max_count = max(max_count, result[i])

for i in range(N):
    if result[i] == max_count:
        answer.append(i+1)

print(' '.join(map(str,answer)))

