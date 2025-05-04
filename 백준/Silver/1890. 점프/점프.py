N = int(input())

graph = [[0]*N for _ in range(N)]

for i in range(N):
    row_data = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = row_data[j]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and graph[i][j] != 0:
            jump = graph[i][j]

            if i + jump < N:
                dp[i+jump][j] += dp[i][j]
            if j + jump < N:
                dp[i][j+jump] += dp[i][j]

print(dp[-1][-1])

