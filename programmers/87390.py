def solution(n, left, right):
    arr = []
    
    for i in range(left, right + 1):
        r1 = i%n 
        r2 = i//n
        
        if r1 > r2:
            arr.append(r1 + 1)
        else:
            arr.append(r2 + 1)
                   
    return arr