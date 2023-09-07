import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
res = []

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    now = q.popleft()
    res.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

print(*res)