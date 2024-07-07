from collections import deque
N, K = map(int, input().split())

def bfs(N, K):
    visited = [0] * 100001
    queue = deque([(N,0)])


    while queue:
        pos, time = queue.popleft()

        if pos == K:
            return time
        for next_pos in (pos + 1, pos -1 ,pos*2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = 1
                queue.append((next_pos, time + 1))
                
    return -1


       
print(bfs(N, K))

            
        
         
        
        
      


