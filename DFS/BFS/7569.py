from collections import deque

M, N, H = map(int, input().split())

graph = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for i in range(N):
        row_data = list(map(int, input().split()))
        for j in range(M):
            graph[h][i][j] = row_data[j]

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    days = 0

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1:
                    queue.append((h, i, j))

    while queue:
        size = len(queue)

        for _ in range(size):
            z, y, x = queue.popleft()

            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                    if graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] = 1
                        queue.append((nz, ny, nx))

        days += 1  

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 0:
                    return -1  

    return days - 1  

print(bfs())
