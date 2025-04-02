H, W, X, Y = map(int, input().split())

A = [[0] * (W) for _ in range(H)]
B = [[0] * (W+Y) for _ in range(H+X)]

for i in range(H+X):
    row_data =input().split()
    for j in range(W+Y):
        B[i][j] = int(row_data[j])

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(X,H):
    for j in range(Y, W):
        A[i][j] -= A[i-X][j-Y]

for row in A:
    print(*row)            
        