from collections import deque

def min_operations(s):
    queue = deque([(1, 0, 0)])
    visited = set((1, 0))
    
    while queue:
        screen, clipboard, steps = queue.popleft()
        
        if screen == s:
            return steps
        
        if (screen, screen) not in visited:
            queue.append((screen, screen, steps + 1))
            visited.add((screen, screen))
        
        if clipboard > 0 and (screen + clipboard, clipboard) not in visited:
            queue.append((screen + clipboard, clipboard, steps + 1))
            visited.add((screen + clipboard, clipboard))
        
        if screen > 1 and (screen - 1, clipboard) not in visited:
            queue.append((screen - 1, clipboard, steps + 1))
            visited.add((screen - 1, clipboard))

s = int(input().strip())

print(min_operations(s))
