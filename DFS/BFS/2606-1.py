N = int(input())
M = int(input())

stack = []

graph = [[] for _ in range(N+1)]

#인접 리스트
for k in range(M):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

affected = [0]*(N+1)
print(graph)

def dfs(v):
    cnt = 0
    stack.append(v)
    affected[v] = 1
    while stack:
        node = stack.pop()
        for val, k in enumerate(graph[node]):
            if affected[k] == 0:
                affected[k] = 1
                stack.append(k)
                cnt += 1
    print(cnt)

dfs(1)

        