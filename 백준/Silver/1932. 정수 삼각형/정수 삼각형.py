import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = g[0][0]

for i in range(1, n):
    for j in range(i+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j] + g[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + g[i][j])
print(max(dp[n-1]))