import sys
input = sys.stdin.readline

MOD = 1_000_000_009

T = int(input())
queries = [int(input()) for _ in range(T)]
maxN = max(queries)

dp = [0] * (maxN + 1)


dp[0] = 1
if maxN >= 1: dp[1] = 1
if maxN >= 2: dp[2] = 2
if maxN >= 3: dp[3] = 2
if maxN >= 4: dp[4] = 3
if maxN >= 5: dp[5] = 3

for n in range(6, maxN + 1):
    dp[n] = (dp[n-2] + dp[n-4] + dp[n-6]) % MOD

out = []
for n in queries:
    out.append(str(dp[n]))
print("\n".join(out))
