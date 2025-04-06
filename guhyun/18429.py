from itertools import permutations

N, K = map(int, input().split())

kits = list(map(int, input().split()))

def cal(combs):
    weight = 500
    for kit in combs:
        weight = weight + kit - K 
        if weight < 500:
            return False
    return True

cnt = 0

for combs in permutations(kits, N):
    if cal(combs):
        cnt += 1

print(cnt)