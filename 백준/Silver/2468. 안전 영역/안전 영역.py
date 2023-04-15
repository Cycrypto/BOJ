import copy
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, graph))

def run(graph, visited, i, j):
    visited[i][j] = 1

    q = deque()
    q.append([i, j])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


def bfs(g, rain):
    graph = copy.deepcopy(g)
    visited = [[0 for _ in range(n)] for __ in range(n)]
    depth = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = graph[i][j] - rain \
                if graph[i][j] >= rain else 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] > 0 and not visited[i][j]:
                depth += 1
                run(graph, visited, i, j)

    return depth
            

area = 0
for rain in range(0, max_height):
    area = max(area, bfs(graph, rain))
print(area)