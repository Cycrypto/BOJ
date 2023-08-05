from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [0]*(n+1)

for i in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

def bfs(k):
    q = deque([k])
    visited[k] = 1
    cnt = 1

    while q:
        c = q.popleft()
        for i in graph[c]:
            if not visited[i]:
                visited[c] = 1
                q.append(i)
                cnt += 1
    return cnt

result = 1
for i in range(1, n+1):
    if not visited[i]:
        result *= bfs(i)
print(result % 1000000007)