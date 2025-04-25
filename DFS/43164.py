from collections import defaultdict, deque

def solution(begin, target, words):
    if target not in words:
        return 0


    graph = defaultdict(list)
    
    def isOneLetterDiff(w1, w2):
        return sum(a != b for a, b in zip(w1, w2)) == 1

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and isOneLetterDiff(words[i], words[j]):
                graph[words[i]].append(words[j])
    
    
    for word in words:
        if isOneLetterDiff(begin, word):
            graph[begin].append(word)

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current, depth = queue.popleft()

        if current == target:
            return depth

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                visited.add(neighbor) 

    return 0
