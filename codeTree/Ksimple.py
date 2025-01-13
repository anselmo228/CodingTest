A = []
B = []

# N 입력
N = int(input())
for i in range(N):
    k = int(input())
    A.append(k)

# M 입력
M = int(input())
for i in range(M):
    k = int(input())
    B.append(k)

cnt = 0

for i in range(N-M+1):
    if sorted(A[i:i+M]) == sorted(B):
        cnt += 1

for i in range(N-M+1):
    if sorted(A[i:i+M]) == sorted(B):
        cnt += 1
    if sorted(A[i:i+M]) == sorted(B, reverse=True):
        cnt +=1

