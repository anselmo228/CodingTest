from collections import deque

N = int(input())
aqua = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

x, y = 0, 0

for i in range(N):
    row_data = input().split()
    for j in range(N):
        aqua[i][j] = int(row_data[j])
        if aqua[i][j] == 9:
            x = i
            y = j
            aqua[i][j] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, shark):
    queue = deque()
    queue.append((x, y))
    eat_list = []
    dp = [[-1] * N for _ in range(N)]
    dp[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and dp[nx][ny] == -1 and aqua[nx][ny] <= shark:
                dp[nx][ny] = dp[x][y] + 1
                if aqua[nx][ny] != 0 and aqua[nx][ny] < shark:
                    eat_list.append((dp[nx][ny], nx, ny))
                else:
                    queue.append((nx, ny))
    return sorted(eat_list, key=lambda x: (x[0], x[1], x[2]))

def moveShark(x, y, shark):
    time = 0
    eat = 0

    while True:
        # bfs 호출로 먹을 수 있는 물고기 리스트를 가져옴
        eat_list = bfs(x, y, shark)
        if not eat_list:  # 먹을 물고기가 없으면 종료
            break

        # 가장 가까운 물고기 선택
        distance, nx, ny = eat_list[0]
        time += distance

        # 상어를 이동시키고 물고기를 먹음
        x, y = nx, ny
        aqua[x][y] = 0
        eat += 1

        # 상어 크기 증가 조건
        if eat == shark:
            shark += 1
            eat = 0

    return time

print(moveShark(x, y, 2))
