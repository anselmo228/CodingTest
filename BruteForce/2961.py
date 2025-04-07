from itertools import combinations

max = 1e9
N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

result = max

for i in range(1, N+1):
    for combs in combinations(ingredients, i):
        s = 1
        b = 0
        for comb in combs:
            s *= comb[0]
            b += comb[1]
        
        result = min(result, abs(s-b))

print(result)