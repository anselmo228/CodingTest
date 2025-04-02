N = int(input())  
switchs = list(map(int, input().split()))  

def boys(k):
    for i in range(k, N, k+1):  
        switchs[i] = 1 - switchs[i]  

def girls(k):
    i = k - 1  
    j = k - 1  

    while i > 0 and j < N - 1 and switchs[i - 1] == switchs[j + 1]:
        i -= 1
        j += 1  

    for n in range(i, j + 1):  
        switchs[n] = 1 - switchs[n]

num = int(input())  
for _ in range(num):
    gender, switch_num = map(int, input().split())
    
    if gender == 1:  
        boys(switch_num - 1)
    else:  
        girls(switch_num)

for i in range(0, N, 20):
    print(*switchs[i:i+20])
