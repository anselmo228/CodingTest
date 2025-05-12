N, K = map(int, input().split())

arr = list(map(int, input().split()))

def cal(L, R, X, arr):
    for i in range(L-1, R):
        arr[i] += X
    arr.sort()

    return arr

if K != 0:
    arr.sort()
    
for _ in range(K):
    L, R, X = map(int, input().split())

    arr = cal(L, R, X, arr)

print(' '.join(str(x) for x in arr))