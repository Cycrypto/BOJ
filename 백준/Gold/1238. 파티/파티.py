import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


n, m, x = map(int, input().split())
g = [[] for _ in range (n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b,c))


def dijkstra(start):
    distance = [INF] * (n + 1)
    hq = []

    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for to, co in g[now]:
            cost = dist + co
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(hq, (cost, to))
    return distance


result = -INF

to = dijkstra(x)

for i in range(1, n+1):
    if i == x:
        continue

    result = max(result, dijkstra(i)[x] + to[i])
print(result)
