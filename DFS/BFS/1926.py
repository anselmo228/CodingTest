from collections import deque

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    row_data = input().split()
    for j in range(m):
        graph[i][j] = int(row_data[j])

list = [0]

count_pic = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                
                visited[nx][ny] = 1
                queue.append((nx, ny))

    list.append(count+1)
         
   

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            visited[i][j] = 1
            bfs(i,j)
            count_pic += 1
    
print(count_pic)
print(max(list))