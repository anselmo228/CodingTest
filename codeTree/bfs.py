from collections import deque
import copy

N = int(input())
graph_col = [list(input().strip()) for _ in range(N)]

graph_noncol = copy.deepcopy(graph_col)
for i in range(N):
    for j in range(N):
        if graph_noncol[i][j] == 'R' or graph_noncol[i][j] == 'G':
            graph_noncol[i][j] = 'O'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, graph, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    color = graph[i][j]
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True

def count_regions(graph):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, graph, visited)
                cnt += 1
    return cnt

normal_regions = count_regions(graph_col)
colorblind_regions = count_regions(graph_noncol)

print(normal_regions, colorblind_regions) 