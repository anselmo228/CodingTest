N = int(input())
costs = list(map(int, input().split()))
M = int(input())

def poss(limit):
    total = 0

    for c in costs:
        total += min(c, limit)
    
    return total <= M

def getHigh():
    left = 0
    right = max(costs)

    result = 0

    while left <= right:
        mid = (left + right) // 2
        if poss(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(getHigh())