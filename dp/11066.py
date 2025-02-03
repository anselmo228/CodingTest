import sys

def findFile():
    dp = [[0] * (K+1) for _ in range(K+1)]

    for i in range(1, K+1):
            dp[i][j] = files[i] + files[j]
    
    for i in range(K-1, 0, -1):
        for j in range(0, K+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][n] + dp[n+1][j] for n in range(i,j)]) + sum(files[i:j+1])
    

    return dp[1][K]

T = int(sys.stdin.readline().strip())

for _ in range(T):
    K = int(sys.stdin.readline().strip())
    files = [0] + list(map(int, sys.stdin.readline().strip().split()))

    print(findFile())
