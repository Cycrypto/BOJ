import sys
input = sys.stdin.readline
n, m = map(int, input().split())
weapon = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0] = weapon[0]

for i in range(1, n):
    for j in range(m):
        result = 9876543210
        for k in range(m):
            if not j == k:
                result = min(result, dp[i-1][k])

        dp[i][j] = weapon[i][j] + result
print(min(dp[-1]))