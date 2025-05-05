N = int(input())

INF = float('INF')
checkpoints = []
checked = []

for _ in range(N):
    check = list(map(int, input().split()))
    checkpoints.append((check[0],check[1]))

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

now_x = checkpoints[0][0]
now_y = checkpoints[0][1]

dist = 0

for i in range(1, N):
    dist += manhattan(now_x, now_y, checkpoints[i][0], checkpoints[i][1])
    now_x = checkpoints[i][0]
    now_y = checkpoints[i][1]

min_dist = INF

for i in range(1,N-1):
    total_dist = dist
    total_dist -= manhattan(checkpoints[i][0], checkpoints[i][1], 
                      checkpoints[i-1][0], checkpoints[i-1][1])
    total_dist -= manhattan(checkpoints[i][0], checkpoints[i][1], 
                      checkpoints[i+1][0], checkpoints[i+1][1])
    total_dist += manhattan(checkpoints[i-1][0], checkpoints[i-1][1], 
                      checkpoints[i+1][0], checkpoints[i+1][1])
    
    min_dist = min(min_dist, total_dist)

print(min_dist)