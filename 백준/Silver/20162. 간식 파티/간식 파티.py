import sys
input = sys.stdin.readline

N = int(input().strip())
g = [0] * (N + 1)

for i in range(1, N + 1):
    g[i] = int(input().strip())

dp = [0] * (N + 1)

ans = 0
for i in range(1, N + 1):
    best_prev = 0
    for j in range(1, i):
        if g[j] < g[i]:
            if dp[j] > best_prev:
                best_prev = dp[j]
    dp[i] = g[i] + best_prev
    if dp[i] > ans:
        ans = dp[i]

print(ans)
