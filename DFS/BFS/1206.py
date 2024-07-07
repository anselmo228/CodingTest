from collections import deque
N,M = map(int, input().split())

graph = [[0]*(M) for _ in range(N)]


for i in range (N):
    row_data = input().split()
    for j in range(M):
        graph[i][j] = int(row_data[j])

queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            next_i, next_j = i + dx[k], j + dy[k]

            if 0 <= next_i < N and 0 <= next_j < M:
                if graph[next_i][next_j] == 1:
                    queue.append((next_i, next_j))
                    graph[next_i][next_j] = graph[i][j] + 1
    return graph[N-1][M-1]
                    

print(max(graph))


    


