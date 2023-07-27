from collections import deque
n = int(input())
graph = [[] for _ in range(10001)]
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    visited = [0 for _ in range(101)]
    cnt = 0
    q = deque([1])
    while q:
        c = q.popleft()
        visited[c] = 1
        for i in graph[c]:
            if visited[i] != 1:
                q.append(i)

    return len(list(filter(lambda x: x==1, visited))) - 1

print(bfs())
