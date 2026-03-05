from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())

g = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))


far_node = 0
far_dist = 0


def dfs(u, parent, dist):
    global far_node, far_dist

    if dist > far_dist:
        far_dist = dist
        far_node = u

    for v, w in g[u]:
        if v == parent:
            continue
        dfs(v, u, dist + w)

dfs(1, -1, 0)
start = far_node
far_dist = 0

dfs(start, -1, 0)
print(far_dist)