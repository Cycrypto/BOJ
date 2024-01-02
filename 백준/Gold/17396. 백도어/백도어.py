import sys
import heapq
INF = float('INF')
input = sys.stdin.readline

n, m = map(int, input().split())
is_seeing = list(map(int, input().split()))
is_seeing[-1] = 0
graph = [[] * m for _ in range(n)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    distance = [INF] * n
    heapq.heappush(q, (0, 0))
    distance[start] = 0
    while q:
        # print("q : ",q)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for to, co in graph[now]:   # to까지 co만큼 비용이 든다
            cost = dist + co
            if is_seeing[to]:
                continue;
            
            if cost < distance[to]: # 이때 새로운 비용이 이전 비용보다 작다면 교체후 집어넣음
                distance[to] = cost
                heapq.heappush(q, (cost, to))

    return distance[-1]

result = dijkstra(0)
print(result if result != INF else -1)