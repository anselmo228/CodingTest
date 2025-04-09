from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)  # 다리의 초기 상태: w 길이만큼 0
time = 0
current_weight = 0
truck_index = 0

while truck_index < n:
    time += 1
    # 다리의 앞쪽에서 트럭 빠짐
    out_truck = bridge.popleft()
    current_weight -= out_truck

    # 다음 트럭이 올라갈 수 있으면 올림
    if current_weight + trucks[truck_index] <= l:
        bridge.append(trucks[truck_index])
        current_weight += trucks[truck_index]
        truck_index += 1
    else:
        bridge.append(0)  # 트럭 안 올라가고 시간만 흐름

# 마지막 트럭이 다리 끝까지 가는 시간 더하기
time += w

print(time)