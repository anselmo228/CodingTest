from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]

# 사과 위치 입력
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1  # 1-based index → 0-based index

# 방향 전환 정보 입력
L = int(input())
directions = deque()
for _ in range(L):
    sec, arrow = input().split()
    directions.append((int(sec), arrow))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move():
    x, y = 0, 0  # 뱀의 머리 위치
    graph[x][y] = -1  # 뱀이 있는 위치
    snake = deque([(x, y)])  # 뱀의 몸을 저장
    time = 0
    direction = 0  # 현재 방향 (동쪽)

    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽 충돌 또는 자기 몸과 충돌
        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == -1:
            return time

        # 이동한 칸에 사과가 있는 경우
        if graph[nx][ny] == 1:
            graph[nx][ny] = -1  # 사과 먹고 몸길이 증가
            snake.append((nx, ny))
        # 이동한 칸이 빈 칸인 경우
        else:
            graph[nx][ny] = -1
            snake.append((nx, ny))
            tail_x, tail_y = snake.popleft()  # 꼬리 제거
            graph[tail_x][tail_y] = 0

        # 머리 위치 갱신
        x, y = nx, ny

        # 방향 전환 처리
        if directions and time == directions[0][0]:
            _, arrow = directions.popleft()
            if arrow == 'D':  # 오른쪽 회전
                direction = (direction + 1) % 4
            elif arrow == 'L':  # 왼쪽 회전
                direction = (direction - 1) % 4

print(move())
