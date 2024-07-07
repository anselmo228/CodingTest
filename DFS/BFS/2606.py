from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for k in range(M):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 컴퓨터 감염여부
affected = [0]*(N+1)

def bfs(v):
    queue = deque()
    cnt = 0
    queue.append(v)
    affected[v] = 1
    while queue:
        node = queue.popleft()
        for val, k in enumerate(graph[node]):
            if affected[k] == 0:
                affected[k] = 1
                queue.append(k)
                cnt += 1
    print(cnt)
            
                
bfs(1)
