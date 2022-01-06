n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0 for _ in range(10000)]
dp[0] = 0
dp[1] = wine[1]
dp[2] = dp[1] + wine[2]

for i in range(3, n):
    dp[i] = max(dp[i-3] + wine[i - 1] + wine[i], dp[i-1] + dp[i-2] + wine[i])
    print(dp[i])

print(dp)