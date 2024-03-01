import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float('INF')
MAX = 10001

graph = defaultdict(list)
distance = [INF] * MAX
s, e = map(int, input().split())

for i in range(e+1):
    graph[i].append((i+1, 1))

for _ in range(s):
    a, b, c = map(int, input().split())
    if b > e:
        continue

    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    cur_dist, node = heapq.heappop(q)
    if distance[node] < cur_dist:
        continue

    for next_node, next_dist in graph[node]:
        dist = cur_dist + next_dist
        if dist < distance[next_node]:
            distance[next_node] = dist
            heapq.heappush(q, (dist, next_node))

print(distance[e])