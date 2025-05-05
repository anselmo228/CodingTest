num = list(map(int, input().split()))

A = []
B = []

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = set(A) - set(B)
result = len(answer)

print(result)
answer = list(answer)
answer.sort()

if result != 0:
    print(' '.join(str(x) for x in answer))