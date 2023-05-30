import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
v = [[0 for _ in range(m)] for __ in range(n)]
dep = [[0 for _ in range(m)] for __ in range(n)]

def bfs(x, y):
    q = deque([[x, y, 0]])
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    while q:
        cx, cy, d = q.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and not g[nx][ny]:
                if v[nx][ny] == 0:
                    v[nx][ny] = 1
                    dep[nx][ny] = d+1
                    q.append([nx, ny, d+1])
                
                else:
                    if dep[nx][ny] <= d+1:
                        continue
                    else:
                        dep[nx][ny] = d+1
                        q.append([nx, ny, d+1])
                    
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 1:
            bfs(i, j)

print(max(sum(dep, [])))
