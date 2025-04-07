from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    values = list(map(int, input().split()))
    
    max_team = max(values) + 1
    score_team = [0 for _ in range(max_team)]

    for i in range(N):
        k = values[i]
        score_team[k] += 1
    
    for i in range(max_team):
        if 0 < score_team[i] < 6:
            values = [x for x in values if x != i]
    
    members = defaultdict(list)

    for i in range(len(values)):
        members[values[i]].append(i + 1)
    
    members = {team: ranks for team, ranks in members.items() if len(ranks) >= 6}

    min_score = 1e9
    fifth_min = 1e9
    index = 0

    for team, scores in members.items():
        scores.sort()
        score = sum(scores[:4])
        
        fifth = scores[4]

        if score < min_score or (score == min_score and fifth < fifth_min):
            min_score = score
            fifth_min = fifth
            index = team
    
    print(index)





