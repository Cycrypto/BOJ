from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[cx][cy] + 1
                    q.append([nx, ny])


n, m = map(int, input().split())
graph = [list(map(lambda x:x-2,map(int, input().split()))) for _ in range(n)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            bfs(i, j)
            break

for i in graph:
    for j in i:
        print(j if j != -2 else 0, end=' ')
    print()