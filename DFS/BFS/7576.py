from collections import deque
M, N = map(int, input().split())

graph = [[0]*(M) for _ in range(N)]

for i in range(N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])


def bfs(graph):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<= nx < N and 0<= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

        
    max_day = 0
    for row in graph:
        for day in row:
            # 안익은게 하나라도 있으면 -1
            if day == 0:
                return -1
            max_day = max(max_day, day)
    return max_day - 1
                

print(bfs(graph))




