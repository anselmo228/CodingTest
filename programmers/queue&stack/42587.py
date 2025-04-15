from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([(i, l) for i, l in enumerate(priorities)])
    
    cnt = 0
    while queue:
        idx, priority = queue.popleft()
        
        if any(priority < other[1] for other in queue):
            queue.append((idx, priority))
        else:
            cnt += 1
            
            if idx == location:
                return cnt
