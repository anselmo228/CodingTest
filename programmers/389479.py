def solution(players, m, k):
    
    servers = []
    result = 0

    def getServers(servers):
        cnt = 0
        for i in range(len(servers)):
            servers[i] += 1 
            if servers[i] < k: 
                cnt += 1
        return cnt
        
    for player in players:
        n = getServers(servers)  # 서버 갯수
        need = player // m  # 필요한 서버 갯수
        
        if need > n and player >= m:
            for _ in range(need - n):
                servers.append(0)  
                result += 1
            
    return result
