M = str(input())
M = list(M)

words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = 0
i = 0

while(i < len(M)-1):

    word = M[i] + M[i+1]
    if word in words:
        n += 1
        i += 2

    elif i < len(M)-2 and word + M[i+2] == 'dz=':
        n += 1
        i += 3
              
    else:
        n += 1
        i += 1

if i == len(M) -1:
    n += 1

print(n)