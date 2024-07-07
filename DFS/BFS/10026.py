import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())

# 그래프 생성
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
graph_con = copy.deepcopy(graph)
visited_con = copy.deepcopy(visited)

for i in range(N):
    for j in range(N):
        if graph_con[i][j] == 'R':
            graph_con[i][j] = 'G'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 돌아주기
def bfs(i, j, graph, visited):
    queue = deque()
    queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
        
    return 1

total_count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            total_count += bfs(i, j, graph, visited)

visited = [[False] * N for _ in range(N)]

total_count_con = 0

for i in range(N):
    for j in range(N):
        if not visited_con[i][j]:
            total_count_con += bfs(i, j, graph_con, visited_con)

print(total_count, total_count_con)
