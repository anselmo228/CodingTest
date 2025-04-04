from collections import deque

N, M = map(int, input().split())

graph = [[0]*M for _ in range(N)]
safeness = [[0]*M for _ in range(N)]

for i in range(N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():

    while queue:
        a, b = queue.popleft()

        x = a
        y = b

        dx = [-1, 1, 0, 0, -1, 1, 1, -1]
        dy = [0, 0, -1, 1, 1, -1, 1, -1]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] == 0:
                    dist = abs(a-nx) + abs(b-ny)
                    if safeness[nx][ny] > dist or safeness[nx][ny] == 0:
                        safeness[nx][ny] = dist
                
                    queue.append((nx,ny))

bfs()

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, safeness[i][j])
print(safeness)
print(answer)