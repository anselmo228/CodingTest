import sys
from collections import deque

deq = deque()

N = int(sys.stdin.readline())

output = []

for i in range(N):
    logic = sys.stdin.readline().split()

    if logic[0] == 'push_front':
        deq.insert(0, int(logic[1]))

    elif logic[0] == 'push_back':
        deq.append(int(logic[1]))

    elif logic[0] == 'pop_front':
        if deq:
            output.append(str(deq.popleft()))
        else:
            output.append("-1")

    if logic[0] == 'pop_back':
        if deq:
            output.append(str(deq.pop()))
        else:
            output.append("-1")

    elif logic[0] == 'back':
        if deq:
            output.append(str(deq[-1]))
        else:
            output.append("-1")

    elif logic[0] == 'front':
        if deq:
            output.append(str(deq[0]))
        else:
            output.append("-1")

    elif logic[0] == 'empty':
        if deq: 
            output.append("0")
        else:
            output.append("1")

    elif logic[0] == 'size':
        output.append(str(len(deq)))
    

print("\n".join(output))
