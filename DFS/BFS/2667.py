from collections import deque

N = int(input())

graph = [[0]*(N) for _ in range(N)]

for i in range(0,N):
    row = input().strip()
    for j in range(0,N):
        graph[i][j] = int(row[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 4가지 위치 이동(상하 좌우로 근처에 있는 값 돌기)
# 추후 중복을 피하기 위해서 이미 1인 값들의 셀은 0으로 변경
def house(i, j):
    count = 0
    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()
        for k in range(4):
            next_i, next_j = i+dx[k],j+dy[k] 
            if 0 <= next_i < N and 0 <= next_j < N and graph[next_i][next_j] == 1:
                queue.append((next_i,next_j))
                graph[next_i][next_j] = 0
                count +=1
    return count

# 시작점 정해주기: 마찬가지로 1인 곳 찾아서 시작. 한번 돌았으면 0으로 초기화
max = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            max.append(house(i, j))

print(len(max))
max.sort()

for i in max:
    print(i)    

    