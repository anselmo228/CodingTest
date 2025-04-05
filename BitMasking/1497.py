import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
guitars = set()

for _ in range(N):
    guitar, songs = input().split()
    songs_2 = ''
    for chr in songs:
        if chr == "Y":
            songs_2 += '1'
        else:
            songs_2 += '0'
    guitars.add(int(songs_2, 2))

# 한곡도 못치는 기타는 제거
guitars -= {0}

# 전부 못치면 -1 출력
if not guitars:
    print(-1)
    exit()

max_cnt = 0

# 만들 수 있는 기타 조합 전부 탐색
# total: 현재까지 연주 가능한 곡수
# num: 새로운 기타가 연주가능한 곡수
for i in range(1, N+1):
    for combs in combinations(guitars, i):
        total = 0
        for num in combs:
            total |= num
        cnt = 0

        for j in range(M):
            if total &(1<<j):
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt
            max_guitar = i
print(max_guitar)