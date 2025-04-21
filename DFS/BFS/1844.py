from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1] 
    
    m = len(maps)        
    n = len(maps[0])     

    
    graph = [[n*m] * n for _ in range(m)]
    graph[0][0] = 0  
    
    def bfs():
        queue = deque([(0, 0)])  
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[nx][ny] == 1 and graph[nx][ny] > graph[x][y] + 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
                        
                        if nx == m - 1 and ny == n - 1:
                            return graph[nx][ny]
        
        return -1
    
    answer = bfs()
    if answer != -1:
        return answer + 1
    return -1
