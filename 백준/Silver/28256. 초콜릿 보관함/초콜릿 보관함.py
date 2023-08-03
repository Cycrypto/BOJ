from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    size = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3 and g[nx][ny] == 'O' and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx, ny])
                size += 1
    return size
                

for i in range(int(input())):
    g = [list(input()) for _ in range(3)]
    visit = [[0 for _ in range(3)] for _ in range(3)]
    visit[1][1] = 1
    cnt = list(map(int, input().split()))
    s = []
    for i in range(3):
        for j in range(3):
            if g[i][j] == 'O' and not visit[i][j]:
                s.append(bfs(i, j))
    if sorted(s) == sorted(cnt[1:]):
        print(1)
    else:
        print(0)
