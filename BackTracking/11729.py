N = int(input())

k = 2**N - 1
print(k)

def hanoi(start, end, N):
    num = 6 - start - end
    if N == 1:
        print(str(start) + " " + str(end))
    else:
        hanoi(start, num, N-1)
        print(str(start) + " " + str(end))
        hanoi(num, end, N-1)

hanoi(1, 3, N)
