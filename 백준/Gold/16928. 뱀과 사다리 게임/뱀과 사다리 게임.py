import heapq

N, M = map(int, input().split())

graph = [[0]*10 for _ in range(10)]

move = {}

for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    move[x] = y

curr = 1
heap = []
heapq.heappush(heap, (0, 1)) 
visited = [False]*101
visited[1] = True


while heap:
    
    cnt, curr = heapq.heappop(heap)

    if curr == 100:
        print(cnt)
        break

    for i in range(1, 7):
        next = curr + i

        if next > 100:
            continue

        # 사다리는 무조건 타고, 뱀은 무조건 피하기
        if next in move:
            ladder = move[next]
            
            next = ladder
 

        if not visited[next]:
            visited[next] = True
            heapq.heappush(heap, (cnt+1, next))
