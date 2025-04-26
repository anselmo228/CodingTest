import heapq

def solution(scoville, K):
    
    heapqlist = []
    for s in scoville:
        heapq.heappush(heapqlist, s)
    
    def findK(heapq):
        for s in heapq:
            if s < K:
                return True
        
        return False
    
    count = 0
    
    while findK(heapqlist):
        
        if len(heapqlist) < 2:  
            return -1
        
        a = heapq.heappop(heapqlist)
        b = heapq.heappop(heapqlist)
        c = a + 2*b

        heapq.heappush(heapqlist, c)
        count += 1
        
    return count