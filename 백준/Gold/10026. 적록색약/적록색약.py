from collections import deque
import copy
def BFS(x, y, f, n, area, visited):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] == f and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


def generate(area, visited, n):
    rgb = [0, 0, 0]
    color = ['R', 'G', 'B']

    for idx, c in enumerate(color):
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == c and visited[i][j] == 0:
                    BFS(i, j, c, n, area,visited)
                    rgb[idx] += 1
    return sum(rgb)

def solve():
    n = int(input())
    area = [list(input()) for _ in range(n)]
    area2 = list(map(lambda row: list(map(lambda x: 'R' if x == 'G' else x, row)), area))
    visited = [[0 for _ in range(n)] for __ in range(n)]
    visited2 = copy.deepcopy(visited)

    print(generate(area, visited, n), generate(area2, visited2, n))

solve()