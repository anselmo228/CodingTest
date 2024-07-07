N, M = map(int, input().split())

graph = [[] for _ in range(N)]
Friend = False

for k in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False for _ in range(N)]

def dfs(v, depth):
    global Friend  

    # 아직 방문하지 않았다면
    if visited[v] == False:
        # 일단 하나 추가
        depth += 1
        visited[v] = True
        
        # 이미 친구 관계가 형성되었다면
        if depth == 4:
            Friend = True
            return Friend  

        # 아직 모자라다면
        else:
            # 인접리스트에서 하나씩
            for k in graph[v]:
                if visited[k] == False:
                    dfs(k, depth)
            visited[v] = False

for i in range(N):
    dfs(i, 0)
    # Friend가 True일때만
    if Fr:
        res = 1
        break
    else:
        res = 0
print(res)
