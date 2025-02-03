from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque([(a,b)])
   
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if i == 0 or 1 and dp[nx][ny] > dp[x][y] + buildings[nx]:
                    dp[nx][y] = dp[x][y] + buildings[nx]
                    queue.append((nx,ny))
            
                if i == 2 or 3 and dp[nx][ny] > dp[x][y] + buildings[ny]:
                    dp[nx][y] = dp[x][y] + buildings[ny]
                    queue.append((nx,ny))
    
    return  min(row[goal-1] for row in dp)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    row_data = input().split()

    buildings = []
    graph = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    dp = [[10**9]*N for _ in range(N)]

    for i in range(N):
        buildings.append(int(row_data[i]))

    for i in range(N):
        dp[i][i] = buildings[i]

    for _ in range(K):
        i, j = map(int, input().split())
        graph[i-1][j-1] = 1
        graph[j-1][1-1] = 1


    goal = int(input())

    print(bfs(0,0))
    print(dp)