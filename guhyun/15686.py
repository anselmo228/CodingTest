from collections import deque
from itertools import combinations
import random

N, M = map(int, input().split())
# M: 최대 치킨집 개수

graph = [[0] * N for _ in range(N)]

for i in range(N):
    row_data = input().split()
    for j in range(N):
        graph[i][j] = int(row_data[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 치킨과 집 사이의 거리 = abs(x1 - x2) + abs(y1 - y2)
def bfs(i, j):
    queue = deque([(i, j)])
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == 2:
                    return abs(nx - i) + abs(ny - j)
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

tot_len = []
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            distance = bfs(i, j)
            if distance is not None:
                tot_len.append(distance)
        elif graph[i][j] == 2:
            chickens.append((i, j))

total = sum(tot_len)
print(total)