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


def dijkstra(start, visit):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for to, co in graph[now]:
            cost = dist + co
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(q, (cost, to))

    return distance[visit]

w1 = dijkstra(1, p1) + dijkstra(p1, p2) + dijkstra(p2, n)
w2 = dijkstra(1, p2) + dijkstra(p1, p2) + dijkstra(p1, n)

print(min(w1,w2) if w1 != INF and w2 != INF else -1)