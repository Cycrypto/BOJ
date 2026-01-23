from collections import deque

n = int(input())
s, e = map(int, input().split())
k = int(input())
visited = [-1 for _ in range(n + 1)]

d = {}
for i in range(k):
    k, v = map(int, input().split())
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = [v]

    if v in d.keys():
        d[k].append(k)

    else:
        d[v] = [k]


def dfs(s, c=0):
    q = deque(d[s])
    visited[s] = c
    # print(visited)
    while (q):
        nx = q.popleft()
        if visited[nx] == -1:
            dfs(nx, c + 1)


dfs(s)
print(visited[e])
