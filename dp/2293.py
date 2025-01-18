n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]
dp[0] = 1
coins = [0 for _ in range(n)]

for i in range(n):
    coins[i] = int(input())

coins.sort()

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])
