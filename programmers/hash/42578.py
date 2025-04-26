from collections import defaultdict

def solution(clothes):
    graph = defaultdict(list)

    for cloth in clothes:
        if cloth[1] not in graph:
            graph[cloth[1]] = []
        graph[cloth[1]].append(cloth[0])
    
    total = 1
    
    for g in graph.values():
        total *= (len(g) + 1)
    
    return total-1