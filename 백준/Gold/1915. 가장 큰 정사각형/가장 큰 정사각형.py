n, m = map(int, input().split())
g = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i >= 1 and j >= 1 and g[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = g[i][j]

size = max(sum(dp, []))
print(size ** 2)