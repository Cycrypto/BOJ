from collections import deque


def BFS(x, y):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])

    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    while q:
        cx, cy = q.popleft()
        for i in range(8):
            nx, ny = dx[i] + cx, dy[i] + cy
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    q.append([nx, ny])

while True:
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for __ in range(h)]
    cnt = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                BFS(i, j)
                cnt += 1
    print(cnt)


