from sys import stdin

max_coin = 10**9 
n, k = map(int, stdin.readline().split())

coins = []
for i in range(n):
   coins.append(int(stdin.readline().rstrip()))
dp = [max_coin] * (k + 1)
dp[0] = 0  

coins.sort()

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] == max_coin:
    print(-1)
else:
    print(dp[k])
