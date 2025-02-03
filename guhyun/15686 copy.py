from itertools import combinations

N,M = map(int, input().split())
graph = [[0]*N for _ in range(N)]

arr = []
houses = []

for i in range(N):
    row_data = input().split()
    for j in range(N):
        graph[i][j] = int(row_data[j])
        if graph[i][j] == 2:
            arr.append((i,j))
        if graph[i][j] == 1:
            houses.append((i,j))

combines = list(combinations(arr, M))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b, combine):
    distance = 0
    min = 10**9
    for combi in combine:
        distance = abs(a-combi[0]) + abs(b - combi[1])
        if distance < min:
            min = distance

    return min
                    
min = 10**9

for combine in combines:
    tot_distance = 0
    
    for house in houses:
        tot_distance += bfs(house[0], house[1], combine)

    if tot_distance < min:
        min = tot_distance



print(min)
    