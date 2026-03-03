from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


parent = [0] * (n + 1)

q = deque([1])
parent[1] = 1

while q:
    c = q.popleft()
    for n in graph[c]:
        if parent[n] == 0:
            parent[n] = c
            q.append(n)

for i in parent[2:]:
    print(i)
