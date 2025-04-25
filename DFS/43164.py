def solution(tickets):
    n = len(tickets)
    visited = [False]*n
    
    answer = []
    
    def dfs(start, path):
        
        if len(path) == n + 1:
            answer.append(path)
            return
            
        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+ [ticket[1]])
                visited[idx] = False
                
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]