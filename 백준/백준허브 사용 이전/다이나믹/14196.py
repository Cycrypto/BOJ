n = int(input())
dp = [float("inf") for i in range(100001)]
dp[2] = dp[5] = 1
dp[4] = 2

for i in range(6, n + 1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[n] if dp[n] != float('inf') else -1)