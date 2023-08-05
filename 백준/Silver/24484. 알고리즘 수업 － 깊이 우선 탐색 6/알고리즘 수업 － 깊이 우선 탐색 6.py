import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

n, m, r = map(int, input().split())
graph = {i+1:[] for i in range(n+1)}
visited = [0]*(n+1)
dd = [-1] * (n+1)
tt = [0] * (n+1)

t = 0
for i in range(m):
    k, v = map(int, input().split())
    graph[k].append(v);   graph[v].append(k)

def dfs(start, d=0):
    global t
    conn = sorted(graph[start], reverse=True)
    t += 1
    visited[start] = 1
    dd[start] = d
    tt[start] = t
    for v in conn:
        if not visited[v]:
            dfs(v, d+1)
    return

dfs(r)
result = 0
for i, j in zip(dd, tt):
    result += i * j

print(result)
    