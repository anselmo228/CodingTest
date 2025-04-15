def solution(s):
    cnt = 0
    
    for index in s:
        if index == "(":
            cnt += 1
        elif index == ")" and cnt > 0:
            cnt -= 1
        else:
            return False
    
    if cnt > 0:
        return False
            

    return True