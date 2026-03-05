n = int(input())
s = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = -float('inf')
dp[n] = s[n]
for i in range(n - 1, 0, -1):
    dp[i] = max(dp[i], dp[i+1]) + s[i]
print(max(dp))