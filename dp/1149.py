N = int(input())

graph = [[0]*3 for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

for i in range(N):
    cost = list(map(int, input().split()))
    for j in range(3):
        graph[i][j] = cost[j]

# 첫번째 집 초기화
dp[0][0] = graph[0][0]
dp[0][1] = graph[0][1]
dp[0][2] = graph[0][2]

min_cost = 0

for k in range(1, N):
    dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + graph[k][0]
    dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + graph[k][1]
    dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + graph[k][2]

    min_cost = min(dp[k][0], dp[k][1], dp[k][2])

print(min_cost)

