from collections import deque
import copy
from itertools import combinations

N, M = map(int, input().split())

graph = [[0] * M for _ in range(N)]
for i in range(N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])

# 바이러스 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스가 침투할 수 있는 루트 찾기
def bfs(test_map):
    queue = deque([(i, j) for i in range(N) for j in range(M) if test_map[i][j] == 2])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and test_map[nx][ny] == 0:
                test_map[nx][ny] = 2
                queue.append((nx, ny))

    global result
    count = sum(row.count(0) for row in test_map)
    result = max(result, count)



# 랜덤하게 3개의 벽 세우기 
x_y = [(x, y) for x in range(N) for y in range(M) if graph[x][y] == 0]
result = 0
for c in combinations(x_y, 3):
    test_map = copy.deepcopy(graph)
    for x, y in c:
        test_map[x][y] = 1
    bfs(test_map)
 
print(result)