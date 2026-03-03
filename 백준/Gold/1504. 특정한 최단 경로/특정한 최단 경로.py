import sys
import heapq
INF = float('INF')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p1, p2 = list(map(int, input().split()))


def dijkstra(start):
    hq = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue

        for to, co in graph[now]:
            cost = dist + co
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(hq, (cost, to))
    return distance


d1 = dijkstra(1)
dp1 = dijkstra(p1)
dp2 = dijkstra(p2)

case1 = d1[p1] + dp1[p2] + dp2[n]
case2 = d1[p2] + dp2[p1] + dp1[n]
ans = min(case1, case2)
print(ans if ans < INF else -1)