from collections import deque

def solution(n, computers):
    def bfs(c):
        queue = deque([c])
        visited[c] = True
        
        while queue:
            now = queue.popleft()
            
            for nextn in range(n):
                if computers[now][nextn] == 1 and not visited[nextn]:
                    visited[nextn] = True
                    queue.append(nextn)
    
    visited = [False]*n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    
    return cnt