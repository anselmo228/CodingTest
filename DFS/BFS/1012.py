from collections import deque

# 상하좌우 이동을 위한 dx, dy 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    # 가로길이 M, 세로길이 N, 배추 위치 개수 K 입력
    M, N, K = map(int, input().split())
    
    # 전체 배추 밭 초기화
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 배추 위치 입력
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    
    # 필요한 배추흰지렁이 수 초기화
    count = 0
    
    # 전체 배추 밭에 대해 탐색
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    print(count)
