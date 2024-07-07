from collections import deque

N, M = map(int, input().split())

graph = [[0]*M for _ in range(N)]

for i in range(N):
    row = input().strip()
    for j in range(M):
        graph[i][j] = int(row[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:

        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0,0))
                





