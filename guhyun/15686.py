from itertools import combinations
from collections import deque
import copy

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

def bfs(a,b, new_graph):
    queue = deque([(a, b)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:

                if new_graph[nx][ny] == 3:
                    return abs(a-nx) + abs(b-ny) 
                else:
                    queue.append((nx,ny))
                    
min = 10**9

for combine in combines:
    new_graph = copy.deepcopy(graph)

    tot_distance = 0
    for combi in combine:
        new_graph[combi[0]][combi[1]] = 3
    for house in houses:
        tot_distance += bfs(house[0], house[1], new_graph)

    if tot_distance < min:
        min = tot_distance
    
    for combi in combine:
        new_graph[combi[0]][combi[1]] = 2


print(min)
    