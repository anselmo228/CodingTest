from collections import deque

N, M = map(int, input().split())

graph = [[0]*M for _ in range(N)]
safeness = [[-1]*M for _ in range(N)]

for i in range(N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))
            safeness[i][j] = 0

def bfs():

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0, -1, 1, 1, -1]
        dy = [0, 0, -1, 1, 1, -1, 1, -1]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<= ny < M:
                if safeness[nx][ny] == -1:
                    safeness[nx][ny] = safeness[x][y] + 1
                    queue.append((nx,ny))

bfs()

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, safeness[i][j])
print(answer)