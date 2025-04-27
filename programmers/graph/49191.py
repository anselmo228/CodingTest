from collections import defaultdict

def solution(n, results):
    answer = 0
    ranks = [-1] * n
    matches_win = defaultdict(list)
    matches_lose = defaultdict(list)
    
    for a, b in results:
        matches_win[a-1].append(b-1)
        matches_lose[b-1].append(a-1)
    
    def dfs_win(start, visited):
        cnt = 0
        for player in matches_win[start]:
            if not visited[player]:
                visited[player] = True
                cnt += 1
                cnt += dfs_win(player, visited)
        return cnt
    
    def dfs_lose(start, visited):
        cnt = 0
        for player in matches_lose[start]:
            if not visited[player]:
                visited[player] = True
                cnt += 1
                cnt += dfs_lose(player, visited)
        return cnt
       
    for i in range(n):
        visited_win = [False] * n
        visited_lose = [False] * n
        win = dfs_win(i, visited_win)
        lose = dfs_lose(i, visited_lose)
        if win + lose == n - 1:
            ranks[i] = lose
    
    for i in range(n):
        if ranks[i] != -1:
            answer += 1
            
    return answer
