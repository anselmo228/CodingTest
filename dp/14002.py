A = int(input())

list = [0 for _ in range(A)]
row_data = input().split()

for i in range(A):
    list[i] = int(row_data[i])

