from collections import deque
R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

booms = deque()


for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                booms.append((i,j))
                
t = 1
while t < N:

    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'
                
    
    t += 1

    if t == N:
        break

    while booms:

        x, y = booms.popleft()

        board[x][y] = '.'

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < R and 0 <= ny < C:
                board[nx][ny] = '.'
    t += 1

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                booms.append((i,j))
    
for row in board:   
    print(''.join(row))