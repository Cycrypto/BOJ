import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dp = [[-1] * m for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] < g[x][y]:
                ways += dfs(nx, ny)

    dp[x][y] = ways
    return ways


print(dfs(0, 0))
