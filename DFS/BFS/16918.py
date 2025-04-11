R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

install_time = [[-1]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            install_time[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while time < N:
    time += 1
    if time % 2 == 0:
        for i in range(R):
            for j in range(C):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    install_time[i][j] = time
    else:
        to_explode = []
        for i in range(R):
            for j in range(C):
                if install_time[i][j] != -1 and time - install_time[i][j] == 3:
                    to_explode.append((i, j))

        for x, y in to_explode:
            board[x][y] = '.'
            install_time[x][y] = -1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if install_time[nx][ny] != -1 and time - install_time[nx][ny] != 3:
                        board[nx][ny] = '.'
                        install_time[nx][ny] = -1

for row in board:
    print(''.join(row))
