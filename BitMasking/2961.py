max = 1e9
N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

result = max

for mask in range(1, 1<<N):
    s = 1
    b = 0
    for i in range(N):
        if mask & (1 << i):
            s *= ingredients[i][0]
            b += ingredients[i][1]
    result = min(result, abs(s-b))
print(result)