import sys
import heapq

input = sys.stdin.readline  
INF = int(1e9)  

N = int(input().strip())  
M = int(input().strip())  

graph = [[] for _ in range(N+1)]  
distance = [INF] * (N+1)  

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  
    distance[start] = 0  

    while q:
        dist, now = heapq.heappop(q)  

        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(start)
print(distance[end])  