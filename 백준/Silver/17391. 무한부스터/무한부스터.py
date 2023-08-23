from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dy = [0, 1]
dx = [1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [[0, 1], [1, 0]]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 0
q = deque([(0, 0)])

while q:
    y, x = q.popleft()
    for i in range(2):
        ny, nx = y, x
        for j in range(board[y][x]):
            ny, nx = ny + dy[i], nx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

print(visited[-1][-1])