import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = [0] * (v+1)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            result[i] = 1
            q.append(i)
    # print(result)
    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = result[now] + 1
            if indegree[i] == 0:
                q.append(i)
    return result

print(*topology_sort()[1:])