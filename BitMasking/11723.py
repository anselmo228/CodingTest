import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    checks = input().split()
    cmd = checks[0]

    if cmd == "add":
        num = int(checks[1])
        S |= (1 << num)
    elif cmd == "remove":
        num = int(checks[1])
        S &= ~(1 << num)
    elif cmd == "check":
        num = int(checks[1])
        print(1 if (S & (1 << num)) else 0)
    elif cmd == "toggle":
        num = int(checks[1])
        S ^= (1 << num)
    elif cmd == "all":
        S = (1 << 21) - 1  
    elif cmd == "empty":
        S = 0
