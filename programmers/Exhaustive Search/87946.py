from itertools import permutations

def solution(k, dungeons):
    answer = -1
    results = []
    lists = []
    for i in range(len(dungeons)):
        lists.append(i)
    
    def findRoute(perm, p):
        cnt = 0
        for j in perm:
            if p >= dungeons[j][0]:
                p -= dungeons[j][1]
                cnt += 1
            else:
                return cnt
        return cnt
        
    for i in range(1, len(dungeons) + 1):
        for perm in permutations(lists, i):
            p = k
            results.append(findRoute(perm, p))
                
    
    return max(results)