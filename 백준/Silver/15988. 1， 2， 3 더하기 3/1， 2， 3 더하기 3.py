import sys
input = sys.stdin.readline

MOD = 1_000_000_009
MAX = 1_000_001

dp = [0] * MAX
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, MAX):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
