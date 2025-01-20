import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = list(map(int, input().split()))

field = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

def findRoute(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    if x == M - 1 and y == N - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    

    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if field[nx][ny] < field[x][y]:
                dp[x][y] += findRoute(nx,ny)
    return dp[x][y]

print(findRoute(0,0))