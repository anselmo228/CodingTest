N, K = map(int, input().split())

MOD = 1_000_000_000  

dp = [[0] * (N + 1) for _ in range(K + 1)]

for n in range(N + 1):
    dp[1][n] = 1

for k in range(2, K + 1):
    for n in range(N + 1):
        dp[k][n] = (dp[k-1][n] + (dp[k][n-1] if n > 0 else 0)) 

print(dp[K][N]%MOD)
