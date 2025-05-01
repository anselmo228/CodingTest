from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0

    while bridge:
        time += 1
        total_weight -= bridge.popleft()

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                total_weight += t
            else:
                bridge.append(0)

    return time
