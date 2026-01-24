import heapq
import sys

input = sys.stdin.readline

INF = float('INF')

v, e = map(int, input().split())
k = int(input())

adj = [[] for _ in range(v + 1)]
dist = [INF] * (v + 1)
dist[k] = 0


for _ in range(e):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

hq = [(0, k)]

while hq:
    d, u = heapq.heappop(hq)

    if d > dist[u]:
        continue

    for b, w in adj[u]:
        nd = d + w
        if nd < dist[b]:
            dist[b] = nd
            heapq.heappush(hq, (nd, b))

for p in dist[1:]:
    print(p if p is not INF else 'INF')
