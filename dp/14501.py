N = int(input())

graph = [[0]*2 for _ in range(N)]


for i in range(N):
    row_data = list(map(int, input().split()))
    for j in range(2):
        graph[i][j] = row_data[j]
print(graph)
dp = [0 for _ in range(N+1)]


for i in range(N): # i 번째 날 상담을 진행했을때
    for j in range(i + graph[i][0], N+1): 
        if dp[j] < dp[i] + graph[i][1]:
            dp[j] = dp[i] + graph[i][1]
print(dp)
print(dp[N])