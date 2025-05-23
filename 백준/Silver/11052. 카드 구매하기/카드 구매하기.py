import sys
input = sys.stdin.readline

N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], (price[j] + dp[i - j]))
print(dp[N])