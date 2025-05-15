from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1 

L = int(input())
directions = deque()
for _ in range(L):
    sec, arrow = input().split()
    directions.append((int(sec), arrow))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move():
    x, y = 0, 0  
    graph[x][y] = -1  
    snake = deque([(x, y)])  
    time = 0
    direction = 0  

    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == -1:
            return time

        if graph[nx][ny] == 1:
            graph[nx][ny] = -1  
            snake.append((nx, ny))

        else:
            graph[nx][ny] = -1
            snake.append((nx, ny))
            tail_x, tail_y = snake.popleft()  
            graph[tail_x][tail_y] = 0


        x, y = nx, ny


        if directions and time == directions[0][0]:
            _, arrow = directions.popleft()
            if arrow == 'D': 
                direction = (direction + 1) % 4
            elif arrow == 'L':  
                direction = (direction - 1) % 4

print(move())
