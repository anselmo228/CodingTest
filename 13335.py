from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

queue = deque()

for i in range(len(trucks)):
    queue.append(trucks[i])

weight = 0
length = 0
time = 0

while queue:
    truck = queue.popleft()
    weight += truck
    length += 1

    if weight > w and length - 1 <= l:
        weight = truck
        length = 1
        time += 1
    elif weight > w and length - 1 > l:
        weight = truck 

print(time)