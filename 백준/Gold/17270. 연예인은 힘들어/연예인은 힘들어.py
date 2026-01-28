import sys, heapq

input = sys.stdin.readline
INF = float('INF')

v, m = map(int, input().split())

g = [[] for _ in range(v + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    g[s].append((e, d))
    g[e].append((s, d))


def dijkstra(g, dist, s):
    hq = [(0, s)]
    while hq:
        current_dist, current_vertex = heapq.heappop(hq)
        if current_dist > dist[current_vertex]:
            continue

        for n_vertex, n_dist in g[current_vertex]:
            next_dist = n_dist + current_dist
            if next_dist < dist[n_vertex]:
                dist[n_vertex] = next_dist
                heapq.heappush(hq, (next_dist, n_vertex))
    return dist


a, b = map(int, input().split())
dist_a = [INF] * (v + 1)
dist_a[a] = 0

dist_b = [INF] * (v + 1)
dist_b[b] = 0

dij_dist_a = dijkstra(g, dist_a, a)
dij_dist_b = dijkstra(g, dist_b, b)


min_dist = INF
for i in range(1, v + 1):
    if i == a or i == b:
        continue
    if dij_dist_a[i] == INF or dij_dist_b[i] == INF:
        continue
    s = dij_dist_a[i] + dij_dist_b[i]
    if s < min_dist:
        min_dist = s

min_dist_a = [INF, -1]
for i in range(1, v+1):

    if i == a or i == b:
        continue
    if dij_dist_a[i] == INF or dij_dist_b[i] == INF:
        continue
    if dij_dist_a[i] + dij_dist_b[i] != min_dist:
        continue
    if dij_dist_a[i] > dij_dist_b[i]:
        continue

    if dij_dist_a[i] < min_dist_a[0]:
        min_dist_a[0] = dij_dist_a[i]
        min_dist_a[1] = i

print(min_dist_a[1])
