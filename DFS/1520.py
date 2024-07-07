import sys
sys.setrecursionlimit(100000)

M, N = map(int, input().split())

graph = []
dp = [[-1]*M for _ in range(N)]

row_data = []
for _ in range(M):
    row_data = list(map(int, input().split()))
    graph.append(row_data)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

count = 0

def dfs(x, y):

    if dp[x][y] != -1:
        return dp[x][y]
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]:
            if nx == M - 1 and ny == N - 1:
                count += 1
            dp[x][y] += dfs(nx, ny)

dfs(0, 0)
print(dp[M-1][N-1])

# dp[x][y] = dp[x-1][y] + dp[x][y-1]