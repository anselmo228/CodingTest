N, S = map(int, input().split())
data = list(map(int, input().split()))

count = 0

def backTracking(k, curr_sum):
    global count
    if k == N:
        return
    
    curr_sum += data[k]
    
    if curr_sum == S:
        count += 1
    
    backTracking(k + 1, curr_sum)
    
    curr_sum -= data[k]
    backTracking(k + 1, curr_sum)

backTracking(0, 0)

print(count)
