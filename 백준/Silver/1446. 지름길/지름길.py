N, D = map(int, input().split())

dp = [i for i in range(D+1)]

ways = []

for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[1] - temp[0] > temp[2] and temp[1] < D+1:
        ways.append(temp)

ways.sort()


for way in ways:
    for i in range(1, D+1):
        if way[1] == i:
            dp[i] = min(dp[i], dp[way[0]]+way[2])

        else:
            dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[D])