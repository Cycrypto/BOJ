import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

V = int(input().strip())
graph = [[] for _ in range(V + 1)]

far_node = 0
far_dist = 0
for _ in range(V):
    arr = list(map(int, input().split()))
    u = arr[0]
    i = 1
    while arr[i] != -1:
        v = arr[i]
        w = arr[i + 1]
        graph[u].append((v, w))
        i += 2


def dfs(u, parent, dist):
    global far_node, far_dist

    if dist > far_dist:
        far_dist = dist
        far_node = u

    for v, w in graph[u]:
        if v == parent:
            continue
        dfs(v, u, dist + w)


dfs(1, -1, 0)
start = far_node
far_dist = 0

dfs(start, -1, 0)
print(far_dist)