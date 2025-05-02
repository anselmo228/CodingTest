number = input().strip()
if number[0] == '0':
    print(0)
    exit()

n = len(number)
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    one_digit = int(number[i-1])
    two_digit = int(number[i-2:i])
    
    if one_digit > 0:
        dp[i] += dp[i-1]
    if 10 <= two_digit <= 26:
        dp[i] += dp[i-2]

print(dp[n] % 1000000)
