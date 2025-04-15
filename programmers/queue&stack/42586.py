from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([(p,s) for p, s in zip(progresses, speeds)])
    
    while queue:
        queue = deque([(p+s,s) for p, s in queue]) 
        
        cnt = 0
        while queue and queue[0][0] >= 100:
            queue.popleft()
            cnt += 1
        
        if cnt:
            answer.append(cnt)
        
    
    
    return answer