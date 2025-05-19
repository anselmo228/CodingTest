from collections import deque

n = int(input())
que = deque()

for i in range(1, n+1):
    que.append(i)

i = 0

while len(que) > 1:
    if i % 2 == 0:
        que.popleft()
    else:
        pop = que.popleft()
        que.append(pop)
    i += 1

print(que[0])


