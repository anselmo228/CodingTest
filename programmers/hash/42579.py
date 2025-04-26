from collections import defaultdict

def solution(genres, plays):
    streamings = defaultdict(list)
    
    answer = []
    for i, genre in enumerate(genres):
        streamings[genre].append((i, int(plays[i])))  
    
    genres_sorted = sorted(streamings.keys(), key=lambda g: -sum(p for i, p in streamings[g]))
    
    for genre in genres_sorted:
        streamings[genre].sort(key=lambda x: (-x[1], x[0]))
        for idx, play in streamings[genre][:2]:
            answer.append(idx)
        
    return answer
