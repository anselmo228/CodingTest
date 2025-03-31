N = int(input())

dp = [[1]*N]
stick = []

for i in range(N):
    a,b = list(map(int, input().split()))
    stick.append([a,b])

stick.sort()

for i in range(1,N):
    for j in range(0,i):
        if stick[j][1] < list[i][1]:
            dp[i] = max(dp[i], dp[j]+1)