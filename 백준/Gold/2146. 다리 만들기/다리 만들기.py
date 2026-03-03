import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
g = list(list(map(int, input().split())) for _ in range(n))
visited = [[-1] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def label_islands():
    island_id = 2
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                q = deque([(i, j)])
                g[i][j] = island_id
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 1:
                            g[nx][ny] = island_id
                            q.append((nx, ny))
                island_id += 1


def shortest_bridge():
    dist = [[-1] * n for _ in range(n)]
    owner = [[0] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if g[i][j] >= 2:
                dist[i][j] = 0
                owner[i][j] = g[i][j]
                q.append((i, j))

    ans = float('INF')
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    owner[nx][ny] = owner[cx][cy]
                    q.append((nx, ny))
                else:
                    if owner[nx][ny] != owner[cx][cy]:
                        ans = min(ans, dist[nx][ny] + dist[cx][cy])
    return ans


label_islands()
print(shortest_bridge())