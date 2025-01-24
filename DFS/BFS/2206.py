from collections import deque

N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
for i in range(N):
    row_data = input().strip()
    for j in range(M):
        graph[i][j] = int(row_data[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    move = [[[0,0]for _ in range(M)] for _ in range(N)]
    move[0][0][0] = 1

    while queue:
        x, y, broken = queue.popleft()

        if x == N - 1 and y == M - 1:
            return move[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                
                if graph[nx][ny] == 1 and broken == 0:
                    move[nx][ny][1] = move[x][y][0] + 1
                    queue.append((nx, ny, 1))

                if graph[nx][ny] == 0 and move[nx][ny][broken] == 0:
                    move[nx][ny][broken] = move[x][y][broken] + 1
                    queue.append((nx, ny, broken))

    return -1

print(bfs())