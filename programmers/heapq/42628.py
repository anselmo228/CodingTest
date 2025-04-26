import heapq

def solution(operations):
    answer = []
    heap = []
    
    def deleteMax(heap):
        for i in range(len(heap)):
            heap[i] = -heap[i]
        heapq.heapify(heap)
        value = -heapq.heappop(heap)
        for i in range(len(heap)):
            heap[i] = -heap[i]
        heapq.heapify(heap)
        return value

    for operation in operations:
        op = operation.split()
        
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
                              
        elif op[0] == "D" and op[1] == "1":
            if heap:
                deleteMax(heap)
                              
        elif op[0] == "D" and op[1] == "-1":
            if heap:
                heapq.heappop(heap)
            
    if not heap:
        answer = [0, 0]
    else:
        answer.append(max(heap))
        answer.append(min(heap))
        
    return answer
