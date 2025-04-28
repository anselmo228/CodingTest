def solution(number, k):
    
    stack = []
    count = 0
    
    number_list = number.strip()
    
    for num in number_list:
        
        while stack and count < k and stack[-1] < num:
            stack.pop()
            count += 1
        stack.append(num)
    
    result = ''.join(stack[:len(stack) - (k - count)])
    
    return result