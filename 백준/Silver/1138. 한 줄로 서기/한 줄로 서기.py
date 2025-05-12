N = int(input())
lines = list(map(int, input().split()))
result = []
for i in range(N -1, -1, -1):
    result.insert(lines[i], i+1)

print(' '.join(str(x) for x in result))