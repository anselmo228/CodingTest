def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        while True:
            for j in range(i+1, len(prices)):
                if prices[i] <= prices[j]:
                    cnt += 1
                else:
                    cnt += 1
                    break
            break
        answer.append(cnt)
        
    return answer