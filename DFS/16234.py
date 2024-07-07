from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    united = []  
    total_population = 0  
    queue = deque([(x, y)])
    united.append((x, y))
    total_population += graph[x][y]
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    united.append((nx, ny))
                    total_population += graph[nx][ny]

    return united, total_population

day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    is_move = False 

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                united, total_population = bfs(i, j, visited)
                if len(united) > 1:
                    avg_population = total_population // len(united)
                    for x, y in united:
                        graph[x][y] = avg_population  
                    is_move = True
            
    if not is_move:  
        break

    day += 1

print(day)
