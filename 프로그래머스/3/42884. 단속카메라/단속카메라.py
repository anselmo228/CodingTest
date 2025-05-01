def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    camera = - 30001
    cnt = 0
    
    for route in routes:
        if route[0] > camera:
            
            cnt += 1
            
            camera = route[1]
    
    
    return cnt