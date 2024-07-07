from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())

graph = [[0] * M for _ in  range(N)]

for i in range(N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(random_map):
    queue = deque([(i, j) for i in range(N) for j in range(M) if random_map[i][j] == 2])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if random_map[nx][ny] == 0:
                    random_map[nx][ny] = 2
                    queue.append((nx, ny))
    global result
    count = sum(row.count(0) for row in random_map)
    result = max(result, count)
                    

# 랜덤하게 벽 세우기
x_y = [(x,y) for x in range(N) for y in range(M) if graph[x][y] == 0]
result = 0

for c in combinations(x_y, 3):
    random_map = copy.deepcopy(graph)
    for x, y in c:
        random_map[x][y] = 1
    # bfs 돌려서 
    bfs(random_map)

print(result)



